import datetime
from haystack import indexes
from limau.models import Recipe

class RecipeIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name_bm = indexes.CharField(model_attr="name_bm")
    created_date = indexes.DateTimeField(model_attr="created_date")

    def get_model(self):
        return Recipe

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(created_date_lte=datetime.datetime.now())