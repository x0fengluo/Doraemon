# Doraemon


```
from Doraemon.Field import *
from Doraemon.Model import Model


class User(Model):
    id = IntegerField('id')
    name = StringField('name')

    class Meta:
        table_name = "table_test"


u = User(id=1, name='laowang')
print(u.save())
```


