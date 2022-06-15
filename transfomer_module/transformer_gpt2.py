from transformers import GPT2Model, GPT2LMHeadModel, GPT2Tokenizer
import re


class GPT2Transformation:

    pass

    def download_model_gpt2lmh(self):

        path_model = "transfomer_module/transformer_models/gpt2lmh/gpt2"
        model = GPT2LMHeadModel.from_pretrained("gpt2")
        model.save_pretrained(path_model)

        path_model = "transfomer_module/transformer_models/gpt2lmh/gpt2_large"
        model = GPT2LMHeadModel.from_pretrained("gpt2-large")
        model.save_pretrained(path_model)

        path_model = "transfomer_module/transformer_models/gpt2lmh/gpt2_xl"
        model = GPT2LMHeadModel.from_pretrained("gpt2-xl")
        model.save_pretrained(path_model)

    def download_model_gpt2(self):

        path_model = "transfomer_module/transformer_models/gpt2/gpt2"
        model = GPT2Model.from_pretrained("gpt2")
        model.save_pretrained(path_model)

        path_model = "transfomer_module/transformer_models/gpt2/gpt2_large"
        model = GPT2Model.from_pretrained("gpt2-large")
        model.save_pretrained(path_model)

        path_model = "transfomer_module/transformer_models/gpt2/gpt2_xl"
        model = GPT2Model.from_pretrained("gpt2-xl")
        model.save_pretrained(path_model)

    def download_tokenizer_gpt2lmh(self):

        path_tokenizer = "transfomer_module/transformer_tokenizer/gpt2"
        tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        tokenizer.save_pretrained(path_tokenizer)

        path_tokenizer = "transfomer_module/transformer_tokenizer/gpt2_large"
        tokenizer = GPT2Tokenizer.from_pretrained("gpt2-large")
        tokenizer.save_pretrained(path_tokenizer)

        path_tokenizer = "transfomer_module/transformer_tokenizer/gpt2_xl"
        tokenizer = GPT2Tokenizer.from_pretrained("gpt2-xl")
        tokenizer.save_pretrained(path_tokenizer)

    def start_gpt2(self, model, model_pretrained, tokenizer):
        '''

        :param model:
        :return:
        '''

        if model == 'gpt2':
            if model_pretrained == 'gpt2':
                path_model = "transfomer_module/transformer_models/gpt2/gpt2"
            elif model_pretrained == 'gpt2_large':
                path_model = "transfomer_module/transformer_models/gpt2/gpt2_large"
            elif model_pretrained == 'gpt2_xl':
                path_model = "transfomer_module/transformer_models/gpt2/gpt2_xl"
        elif model == 'gpt2lmh':
            if model_pretrained == 'gpt2':
                path_model = "transfomer_module/transformer_models/gpt2lmh/gpt2"
            elif model_pretrained == 'gpt2_large':
                path_model = "transfomer_module/transformer_models/gpt2lmh/gpt2_large"
            elif model_pretrained == 'gpt2_xl':
                path_model = "transfomer_module/transformer_models/gpt2lmh/gpt2_xl"

        if tokenizer == 'gpt2':
            path_tokenizer = "transfomer_module/transformer_tokenizer/gpt2"
        elif tokenizer == 'gpt2_large':
            path_tokenizer = "transfomer_module/transformer_tokenizer/gpt2_large"
        elif tokenizer == 'gpt2_xl':
            path_tokenizer = "transfomer_module/transformer_tokenizer/gpt2_xl"

        tokenizer = GPT2Tokenizer.from_pretrained(path_tokenizer)
        model = GPT2LMHeadModel.from_pretrained(path_model, pad_token_id=tokenizer.eos_token_id)

        return tokenizer, model

    def translate_to_english(self, tweet, model='gpt2lmh', model_pretrained='gpt2', tokenizer='gpt2'):
        '''

        :param tweet:
        :param model:
        :param model_pretrained:
        :param tokenizer:
        :return:
        '''

        tokenizer, model = self.start_gpt2(model, model_pretrained, tokenizer)

        sentence = f"Translate following tweet to english: {tweet}"
        input_ids = tokenizer.encode(sentence, return_tensors='pt')

        output = model.generate(input_ids,
                                max_length=300,
                                num_beams=5,
                                no_repeat_ngram_size=2,
                                early_stopping=True)

        tweet_translated = tokenizer.decode(output[0], skip_special_tokens=True)

        return tweet_translated

    def emotion_of_text(self, tweet, model='gpt2lmh', model_pretrained='gpt2', tokenizer='gpt2'):
        '''

        :param tweet:
        :param model:
        :param model_pretrained:
        :param tokenizer:
        :return:
        '''

        tokenizer, model = self.start_gpt2(model, model_pretrained, tokenizer)

        sentence = f"What is the emotion transmitted by following tweet: {tweet}"
        input_ids = tokenizer.encode(sentence, return_tensors='pt')

        output = model.generate(input_ids,
                                max_length=300,
                                num_beams=5,
                                no_repeat_ngram_size=2,
                                early_stopping=True)

        emo_analysis_respond = tokenizer.decode(output[0], skip_special_tokens=True)

        return emo_analysis_respond
