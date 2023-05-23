## Example of Elasticsearch query


<div align="right">یک نمونه داده به داکیومنت اضافه شود.</div>

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
با آی دی دلخواه ایجاد شود
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
ندیس همزمان اضافه، حذف و آپدیت شود
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

نام کشورهایی را برگرداند که تعداد رفتگان در بازه ی 10000 تا 20000 باشد  در ماه دوم سال باشد و تعداد نمونه ها  از 2 برابر تعداد رفتگان بیشتر باشد.
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


تعداد ثبت ها از هر کشور که در ماه سوم ثبت شده اند را نشان دهد.
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


 در بازه های به طول 70000، چه تعداد افراد فوت کرده اند.
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
اضافه کردن فیلد واکسن به کشور ایران
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
تعداد جانباختگان کشور ایران فقط
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
در مجموع از هر کشور چند نفر جانباخته اند؟
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

اندیس هایی بر گردد که در عنوان آن ها یکی از دو نام پایتون، جاوا یا راهنما باشد
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

حذف فیلد شمارش تگ ها
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
