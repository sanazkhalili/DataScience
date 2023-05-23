## Example of Elasticsearch query


1)یک نمونه داده به داکیومنت اضافه شود.

```
PUT covid/_doc/120
{
  "date":"2021-06-02",
  "cases": "1200",
  "country":"Djibouti",
  "deaths":0,
  "recoverd":100
}
```
2)با آی دی دلخواه ایجاد شود.
```
POST covid/_doc
{
  "date":"2021-06-02",
  "cases": "1200",
  "country":"Djibouti",
  "deaths":0,
  "recoverd":100
}
```
3)اندیس همزمان اضافه، حذف و آپدیت شود.
```
POST _bulk
{"index":{"_index":"covid", "_id":"111"}}
{  "date":"2021-04-02","cases": "5000", "country":"Djibouti", "deaths":0,"recoverd":3000}
{"delete":{"_index":"covid", "_id":"111"}}
{"update":{"_index":"covid", "_id":"120"}}
{"doc":{"cases":"5"}}
{"create":{"_index":"covid", "_id":"852"}}
{"date":"2021-07-02","cases": "6000", "country":"Turkey", "deaths":3,"recoverd":6000}
```

4)نام کشورهایی را برگرداند که تعداد رفتگان در بازه ی 10000 تا 20000 باشد  در ماه دوم سال باشد و تعداد نمونه ها  از 2 برابر تعداد رفتگان بیشتر باشد
```
GET covid/_search
{
  "query": {
    "bool": {
      "must": [
        {"range": {
          "deaths": {
            "gte": 90000,
            "lte": 100000
          }
        }},
        {"range": {
          "date": {
            "gte": "2021-03-01",
            "lte": "2021-03-30"
          }
        }},
        {"script": {
          "script": "doc['deaths'].value * 2 < doc['cases'].value"
        }}
      ]
    }
  }
}
```

5)تعداد ثبت ها از هر کشور که در ماه سوم ثبت شده اند را نشان دهد.
```
GET covid/_search
{
  "size": 0,
  "query": {
    "range": {
      "date": {
        "gte": "2021-03-01",
        "lt": "2021-04-01"
      }
    }
  }, 
  "aggs": {
    "counter_country": {
      "terms": {
        "field": "country.keyword"
      }
    }
  }
}
```


6) در بازه های به طول 70000، چه تعداد افراد فوت کرده اند.

```
GET covid/_search
{
  "size": 0, 
  "aggs": {
    "create_range": {
      "histogram": {
        "field": "deaths",
        "interval": 70000
      }
    }
  }
}
```

کدام یک از اندیس ها فیلد واکسن را دارند
```
GET covid/_search
{
  "query": {
    "exists": {"field": "anti"}
  }
}
```
7)اضافه کردن فیلد واکسن به کشور ایران.
```
POST covid/_update_by_query
{
  "query": {
    "match_phrase_prefix": {
      "country": "Ir"
    }
  },
  "script": {
    "source": "ctx._source.anti='True'",
    "lang": "painless"
  }
}
```
8)تعداد جانباختگان کشور ایران فقط.
```
GET covid/_search
{
  "query": {
    "term": {
      "country.keyword": {
        "value": "Iran"
      }
    }
  }
}
```
9)در مجموع از هر کشور چند نفر جانباخته اند؟
```
GET covid/_search
{
  "size": 0,
  "aggs": {
        "countries": {
              "terms": {
                "field": "country.keyword",
                "size": 1000 
              },
              "aggs": {
                "total_deaths": {
                  "sum": {
                    "field": "deaths"
                  }
                }
              }
        }
  }
}
```
or 
```
POST books/_update_by_query
{
  
    "query": {
    "bool": {
      "must": [
        {"exists": {"field": "tags"}}
      ]
    }},
    "script": {
    "source": "ctx._source.tag_number=ctx._source.tag.length()",
    "lang": "painless"
  }
}
```

10)اندیس هایی بر گردد که در عنوان آن ها یکی از دو نام پایتون، جاوا یا راهنما باشد.
```
GET books/_search
{
  "query": {
    "query_string": {
      "fields": ["title"],
      "query": "java guide python",
      "minimum_should_match": "2"
    }
  }
}
```

11)حذف فیلد شمارش تگ ها.
```
POST books/_update_by_query
{
  
    "query": {
    "bool": {
      "must": [
        {"exists": {"field": "tags"}}
      ]
    }},
    "script": {
    "source": "ctx._source.remove(ctx._source.tag_number)",
    "lang": "painless"
  }
}
```

12)مقدار year اندیسی که id آن PvkKl4YBI3fidKnBlJpW است از 26-03-2021 به 02-02-2022 تغییر کند.
```
POST covid/_update/PvkKl4YBI3fidKnBlJpW
{
  "script": {"source": "ctx._source.year='2022-02-02'"}
}
```

```
GET covid/_doc/PvkKl4YBI3fidKnBlJpW
```

14)ساخت runtime field
```
POST covid/_mapping
{
  "runtime": {
    "FIELD2": {
      "type": "long",
      "script": {
        "source": "if (doc['deaths'].size() > 0){emit(doc['deaths'].value)}"
      }
    }
  }
}
```
15) ساخت template
```
PUT _component_template/temp_mapp
{
  "template": {
    "mappings": {
      "properties": {
        "name":{"type": "text"},
        "time":{"type": "date"}
      }
    }
  }
}
```
```
PUT _component_template/temp_setting
{
  "template": {
    "settings": {
      "number_of_shards": 2,
      "number_of_replicas": 2
    }
  }
}
```
```
PUT _component_template/temp_alias
{
  "template": {
    "aliases": {
      "test_temp_alias": {
        "filter": {
          "range": {
            "date": {
              "gte": "2021-02-03",
              "lte": "2021-04-03"
            }
          }
        }
      }
    }
  }
}

```
```
PUT _index_template/temp_index
{
  "index_patterns": ["*user"],
  "composed_of":["temp_alias", "temp_setting","temp_mapp"],
  "priority":500
}
```
```
PUT student_user
```
```
GET stdent_user
```
16)ساخت آنالایزر
```
PUT my-index-000001
{
   "settings":{
      "analysis":{
         "analyzer":{
            "my_analyzer":{ 
               "type":"custom",
               "tokenizer":"standard",
               "filter":[
                  "lowercase"
               ]
            },
            "my_stop_analyzer":{ 
               "type":"custom",
               "tokenizer":"standard",
               "filter":[
                  "lowercase",
                  "english_stop"
               ]
            }
         },
         "filter":{
            "english_stop":{
               "type":"stop",
               "stopwords":"_english_"
            }
         }
      }
   },
   "mappings":{
       "properties":{
          "title": {
             "type":"text",
             "analyzer":"my_analyzer", 
             "search_analyzer":"my_stop_analyzer", 
             "search_quote_analyzer":"my_analyzer" 
         }
      }
   }
}
```


17)ساخت یک alias
```
POST _aliases
{
  "actions": [
    {
      "add": {
        "index": "test_index",
        "alias": "alias2",
        "filter": {
          "range": {
            "number": {
              "gte": 10,
              "lte": 20
            }
          }
        }
      }
    }
  ]
}
```

18)عمل upsert
```
POST covid/_update/QPkKl4YBI3fidKnBlJpW1
{
  "script": {"source": "ctx._source.name='Russia'"},
  "upsert": {
    "name":"san"
  }
}


GET covid/_search
{
  "query": {
    "match": {
      "name": "san"
    }
  }
}
```

20)متفرقه
```
GET covid/_search
{
  "query": {
    "fuzzy": {
      "country.keyword": {
        "value": "Ita", 
        "fuzziness": 2
      }
    }
  }
}
```
differnet wildcard and regex
https://reqchecker.eu/manual/extract_syntax.html
```
GET covid/_search
{
  "query": {
    "wildcard": {
      "country.keyword": {
        "value": "I*"
      }
    }
  }
}
```

```
GET covid/_search
{
  "query": {
    "regexp": {
      "country.keyword": "I[a-z]*"
    }
  }
}
```
