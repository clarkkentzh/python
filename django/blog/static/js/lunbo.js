var box = $("#box-id");

var images = $("#img-id");
var imgWidth = box.width();

var lis = images.children();//li标签数组

var point = $("#point-id");
for (var i = 0; i < lis.length; i++){
  $("<span>").appendTo(point);
}

var spans = point.children();
spans.eq(0).addClass("current");

var timer = null;
var ul_num = 0, span_num = 0;//用于控制要播放那张图片的索引

for (var i = 0; i < spans.length; i++){
  spans.eq(i).on("click", i, function(event){
    $(this).addClass("current").siblings('span').removeClass("current");

    // lis.eq(event.data).fadeIn().siblings("li").fadeOut();

    lis.eq(event.data).addClass("current").siblings("li").removeClass("current");
    ul_num = span_num = event.data ;//让点击播放和自动播放关联起来
  });
}


timer = setInterval(play, 2000);
function play(){
  ul_num++;
  if (ul_num > spans.length - 1){
    ul_num = 0;
  }                             //从最后一张循环回到第一张

  lis.eq(ul_num).addClass("current").siblings("li").removeClass("current");

  span_num++;
  if (span_num > spans.length - 1){
    span_num = 0;
  }
  spans.eq(span_num).addClass("current").siblings('span').removeClass("current");
}

box.hover(function(){
  clearInterval(timer);
}, function(){
  timer = setInterval(play, 2000);
});
