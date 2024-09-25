from transformers import BertTokenizer, BertForSequenceClassification
import torch

class TextGradingModel:
    def _init_(self):
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.model = BertForSequenceClassification.from_pretrained('bert-base-uncased')

    def grade(self, text):
        inputs = self.tokenizer(text, return_tensors='pt')
        outputs = self.model(**inputs)
        scores = torch.nn.functional.softmax(outputs.logits, dim=-1)
        return scores