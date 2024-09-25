from torchvision import models, transforms
from PIL import Image
import torch

class ImageGradingModel:
    def _init_(self):
        self.model = models.resnet50(pretrained=True)
        self.model.eval()
        self.transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])

    def grade(self, image_path):
        image = Image.open(image_path)
        image = self.transform(image).unsqueeze(0)
        with torch.no_grad():
            outputs = self.model(image)
        scores = torch.nn.functional.softmax(outputs, dim=1)
        return scores