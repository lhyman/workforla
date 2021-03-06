from elasticsearch_dsl import DocType
from elasticsearch_dsl import Integer
from elasticsearch_dsl import Text


class JobClassIndex(DocType):
    alias = Text()
    title = Text()
    description = Text()
    qualifications = Text()
    responsibilities = Text()
    categories = Text()
    skills = Text()
    related_keywords = Text()
    salary_low = Integer()
    salary_high = Integer()

    class Meta:
        index = 'jobs'
