"""配置文件

"""

#站点设置
conf = {
    #分页中每页显示影片数量
    'MOVIE_NUM': 10,
    #分类中显示的分类数目
    'GENRES_NUM': 100,
    'YEAR': {
        'start': 1930,
        'end': 2014,
    },
    'HOT_MOVIE': {
        #显示数目
        'num': 12,
        #最低点击数目
        'hot': 3,
    }
}

#系统设置
settings = {
    "app": 'Bastogne',
    "template_path": "templates",
    "static_path": "static",
    "cookie_secret": "enter cookie secret",
    "login_url": "/auth/login",
    "xsrf_cookies": True,
    "debug": True,
}

redis = {
    'host': 'localhost',
    'port': 6379,
    'db': 0,
}

#百度统计代码
tongji_code = """
<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "//hm.baidu.com/hm.js?17e53dc7f7c5656f087d3226386d48de";
  var s = document.getElementsByTagName("script")[0];
  s.parentNode.insertBefore(hm, s);
})();
</script>
"""

#Google adsense
ad1 = """
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- ad4 -->
<ins class="adsbygoogle"
     style="display:inline-block;width:300px;height:250px"
     data-ad-client="ca-pub-7388149537279492"
     data-ad-slot="5946370724"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
"""

ad2 = """
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- ad10 -->
<ins class="adsbygoogle"
     style="display:inline-block;width:300px;height:600px"
     data-ad-client="ca-pub-7388149537279492"
     data-ad-slot="9735721717"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
"""

ad3 = """
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- ad1 -->
<ins class="adsbygoogle"
     style="display:inline-block;width:728px;height:90px"
     data-ad-client="ca-pub-7388149537279492"
     data-ad-slot="6392378150"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
"""

ad_code = [ad1, ad2, ad3]