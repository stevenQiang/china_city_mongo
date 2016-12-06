##中国城市地址
  本来已经从政府网站爬好了，但发现香港，澳门，台湾地址不全，后来发现[china-city]这位兄弟里面很全，所以就借鉴了一下。
  province.txt:省级地址，city.txt:市级地址 county.txt: 县级地址
  介绍格式: province_1,49,北京市     id,国家,名称
        city_id_1,49,province_1,北京市   id,国家,所属省级地址id,名称
        county_id_1,49,province_1,city_id_1,东城区     id,国家,所属省级地址,所属市级地址,名称
  主要用于mongodb.
  特意保存一下，以防后期项目需要。


[china-city]: https://github.com/SSOOnline/china-city/
