import re
import os
import csv
import openai
from openai import OpenAI

#prompts are stored as a list in a separate python file for ease of readbility and ease of changability, without having to touch this main code
from prompts import CxNLI_prompts
from prompts import CxReasoning_prompts

from tqdm            import tqdm
from sklearn.metrics import f1_score

class runTests_NLI :

    def __init__( self, test_data_location, train_data_location, output_location, openai_completion_style, api_path, train_data_version ) :

        self.output_location         = output_location
        self.openai_completion_style = openai_completion_style
        self.api_path = api_path
        
        self.test_data = self._collate_data(self._load_data( test_data_location ), True)
        self.train_data = self._collate_data(self._load_data( train_data_location ), False)
        self._load_openai_key()
        self.train_data_version = train_data_version

        return 

    def _load_data( self, file_location ) :
        header = None
        data   = list()
        path, extension = os.path.splitext(file_location)
        with open( file_location ) as csvfile :
            if extension == ".csv":
                reader = csv.reader(csvfile)
            elif extension == ".tsv":
                reader = csv.reader(csvfile, delimiter="\t")
            for row in reader:
                if header is None:
                    header = row
                    continue
                data.append( row )
        return data

    def _collate_data(self, data, isTestData):
        ## Collate
        if isTestData:
            out_data = list()
        else:
            out_data = dict()
        for i in range( 0, len(data), 3 ) :

            this_cxg = data[i][0]
            assert this_cxg != ''
            assert data[i][2] in [ 'Premi', 'premise' ]
            this_premise = data[i][3]
            assert data[i+1][2] == 'hypothesis'
            this_hypothesis = data[i+1][3]
            assert data[i+2][2] == 'relation'
            this_relation   = data[i+2][3]
            if isTestData:
                this_relation   = int( re.sub( r'\(.*\)', '', this_relation ) ) 
                this_trip = [this_cxg, this_premise,this_hypothesis, this_relation]
                out_data.append(this_trip)
            else:
                this_relation   = re.sub( r'\(.*\)', '', this_relation ) 
                this_trip = "\n" + "Example Premise " + str(i//3+1) +": "+ this_premise +"\n" + "Example Hypothesis " + str(i//3+1) +": " + this_hypothesis+"\n" + "Example Relation Output " + str(i//3+1) +": " + this_relation + "\n"
                #print( this_premise,this_hypothesis + this_relation)
                current_example = out_data[this_cxg] if this_cxg in out_data.keys()  else ""
                out_data[this_cxg] =  current_example + this_trip 
        return out_data
    
    
    def _load_openai_key( self ) :
        with open( self.api_path ) as fh :
            data = fh.readlines()
            self.user_key, self.org_key = data[0].split( ',' )
        openai.organization = self.org_key
        openai.api_key = self.user_key
        return


    def _generate_prompt( self, prompt_number, examples_type ) :

        prompts = CxNLI_prompts.prompts
        question_bit= """
Premise: {}
Hypothesis: {}
Relation: """        
        
        match self.train_data_version:
            case "SNLI":
                prompt = prompts[ prompt_number ] + self.train_data[ "None" ] + question_bit
            case "zero":
                prompt = prompts[ prompt_number ] + question_bit
            case "CoGS-NLI":
                try:
                    prompt = prompts[ prompt_number ] + self.train_data[ examples_type ] + question_bit
                except KeyError:
                    prompt = prompts[ prompt_number ] + question_bit 
            case _:
                print("Please provide a train data version, options are: \"SNLI\", \"zero\" and \"CxNLI\"")
                exit(1)

        return prompt

    def _gpt_get( self, model, prompt, temperature) :
        client = OpenAI(api_key=self.user_key)
        if self.openai_completion_style == 'ChatCompletion' :
            try:
                chat_completion = client.chat.completions.create(
                    model=model,
                    seed=43,
                    temperature=temperature,
                    messages=[{"role": "user", "content": prompt}]
                )
                response = chat_completion.choices[0].message.content
            except Exception as err:
                response = err

        elif self.openai_completion_style == 'Completion' :
            completion = openai.Completion.create(
                model=model,
                temperature=0,
                prompt=prompt,
            )
            response = completion.choices[0].message.content
        
        return response
        
    def get_all( self, model, prompt_number, experiment, temperature) :

        schematicity = { 'let-alone'            : 'substantive', 
                         'way-manner'           : 'partial',
                         'resultative'          : 'schematic', 
                         'conative'             : 'partial',
                         'intransitive motion'  : 'schematic',
                         'intransitive-motion'  : 'schematic',
                         'caused-motion'        : 'schematic',
                         'causative - with'     : 'partial',
                         'causative-with-CxN'   : 'partial',
                         'ditransitive'         : 'schematic',
                         'ditransitive-CxN'     : 'schematic',
                         'comparative-correlative':'comparative-correlative',
                        }
        
        results   = {
            'substantive' : { 'gold' : list(), 'got' : list() }, 
            'partial'     : { 'gold' : list(), 'got' : list() }, 
            'schematic'   : { 'gold' : list(), 'got' : list() }, 
            'all'         : { 'gold' : list(), 'got' : list() }, 
        }

        results_by_row = [ [ 'CxG', 'schematicity', 'Premise', 'Hypothesis', 'Gold', 'Prediction' ] ]
        for row in tqdm( self.test_data ) :
            
            this_schematicity = schematicity[ row[0] ]

            prompt = self._generate_prompt( prompt_number, row[0] )
            prompt = prompt.format( row[1], row[2] )
            
            response = self._gpt_get( model, prompt , temperature)

            # if prompt_number!=5:
            #     try : 
            #         response = int( response )
            #     except ValueError:
            #         response = 10

            results_by_row.append( [ row[0], this_schematicity, row[1], row[2], row[3], response ] )

        outfile = os.path.join( self.output_location, "output_{}_{}_prompt{}.csv".format( model, experiment, prompt_number ) )
        with open( outfile, 'w' ) as csvoutfile :
            writer = csv.writer( csvoutfile )
            writer.writerows( results_by_row )

            print( "Wrote " + outfile )

        return
            

