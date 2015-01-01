
function define (f) {

  var args = Array.prototype.slice.call(arguments, 1);

  f.apply(this, args);

}


define(function (window, $) {

  var TrainStatus = window.TrainStatus = {

    /**
     * 根据是否生成userId进行重定向
     *
     * @public
     */
    redirect: function () {

      var rsearch = /userId=([^\&]+)/;
      var search = window.location.search;
      var userId = window.localStorage.getItem("userId");

      if ( !userId ) {
        tmp = rsearch.match(search);
        userId = tmp && tmp[1];
        userId && window.localStorage.setItem("userId", userId);
      }
      else if ( !search ) {
        window.location.search = "?userId=" + userId;
      }

    }

  };


  // 加载完成回调
  $(window).on("load", function () {

    TrainStatus.redirect();

  });

}, window, jQuery);



define(function (window, module, $) {

  var template = "<li class=\"item finished\">" + 
                    "<span class=\"bubble timepoint\"></span>" + 
                    "<h4 class=\"station\">" + 
                      "$station" + 
                      "<span class=\"bubble stat-ontime\"></span>" + 
                    "</h4>" + 
                    "<p class=\"text-muted\">" + 
                      "<em>计划到达：</em><strong>10:00</strong> 2015-2-18" + 
                    "</p>" + 
                    "<p>" + 
                      "<em>实际到达：</em><strong>10:00</strong> 2015-2-18" +
                    "</p>" + 
                  "</li>";
  var testJSON = {
    isFinished: true,
    isOnTime: true,
    station: "北京"
  };

  /**
   * 火车列表视图控制器
   *
   * @param {jQuery} jQuery的元素查询结果集
   * @class TrainStatus.TrainList
   */
  var TrainList = module.TrainList = function ($view) {
    
    if ( !$view || !$view.length ) {
      return null;
    }

    this.$dom = $view;
    this.trainId = $view.data("trainid");

    this.initEvent();

  };

  TrainList.prototype = {

    constructor: TrainList,

    trainId: null,

    /**
     * 初始化事件监听
     *
     * @public
     */
    initEvent: function () {

      var self = this;

      this.$dom
        // 加载全部
        .on("click.btn", "#LoadAllBtn", function (e) {
          self.loadAllStation();
        })
        .on("click.train", "#List a[data-role='Station']", function (e) {
          var station = this.innerHTML;
          var $parent = $(this).parent();
          self.loadDetail(station, $parent);
        });

    },

    /**
     * 加载一个车次的全部站点信息
     *
     * @public
     */
    loadAllStation: function () {},

    /**
     * 加载某一个站的准点信息
     * 
     * @param {String} station 车站名称
     * @param {jQuery} $node   车站节点jQuery对象
     * @public
     */
    loadDetail: function (station, $node) {}

  };

}, window, TrainStatus, jQuery);