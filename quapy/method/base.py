from abc import ABCMeta, abstractmethod


# Base Quantifier abstract class
# ------------------------------------
class BaseQuantifier(metaclass=ABCMeta):

    @abstractmethod
    def fit(self, data, *args): ...

    @abstractmethod
    def quantify(self, instances, *args): ...

    @abstractmethod
    def set_params(self, **parameters): ...

    @abstractmethod
    def get_params(self, deep=True): ...


# class OneVsAll(AggregativeQuantifier):
#     """
#     Allows any binary quantifier to perform quantification on single-label datasets. The method maintains one binary
#     quantifier for each class, and then l1-normalizes the outputs so that the class prevelences sum up to 1.
#     """
#
#     def __init__(self, binary_method, n_jobs=-1):
#         self.binary_method = binary_method
#         self.n_jobs = n_jobs
#
#     def fit(self, data: LabelledCollection, **kwargs):
#         assert not data.binary, f'{self.__class__.__name__} expect non-binary data'
#         assert isinstance(self.binary_method, BaseQuantifier), f'{self.binary_method} does not seem to be a Quantifier'
#         self.class_method = {c: deepcopy(self.binary_method) for c in data.classes_}
#         Parallel(n_jobs=self.n_jobs, backend='threading')(
#             delayed(self._delayed_binary_fit)(c, self.class_method, data, **kwargs) for c in data.classes_
#         )
#         return self
#
#     def quantify(self, X, *args):
#         prevalences = np.asarray(
#             Parallel(n_jobs=self.n_jobs, backend='threading')(
#                 delayed(self._delayed_binary_predict)(c, self.class_method, X) for c in self.classes
#             )
#         )
#         return F.normalize_prevalence(prevalences)
#
#     @property
#     def classes(self):
#         return sorted(self.class_method.keys())
#
#     def set_params(self, **parameters):
#         self.binary_method.set_params(**parameters)
#
#     def get_params(self, deep=True):
#         return self.binary_method.get_params()
#
#     def _delayed_binary_predict(self, c, learners, X):
#         return learners[c].quantify(X)[:,1]  # the mean is the estimation for the positive class prevalence
#
#     def _delayed_binary_fit(self, c, learners, data, **kwargs):
#         bindata = LabelledCollection(data.instances, data.labels == c, n_classes=2)
#         learners[c].fit(bindata, **kwargs)

