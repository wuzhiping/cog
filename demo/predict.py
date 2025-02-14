from cog import BasePredictor, Input, Path

class Predictor(BasePredictor):
    def setup(self):
        """Load the model into memory to make running multiple predictions efficient"""

    # The arguments and types the model takes as input
    def predict(self,
          image: str= Input(description="Grayscale input image")
    ) -> str:
        """Run a single prediction on the model"""
        output = image
        return output
