from abc import ABC, abstractmethod

class NormalizerInterface(ABC):
    """
    Base interface for stain normalizers.
    """

    @abstractmethod
    def fit(self, target):
        """
        Fits the normalizer to a target image.
        :param target: Reference image for normalization.
        """
        pass

    @abstractmethod
    def transform(self, I):
        """
        Applies normalization to a new image.
        :param I: Image to be normalized.
        :return: Normalized image.
        """
        pass
