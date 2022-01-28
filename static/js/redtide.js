window.onload = function () {
    var nav = document.getElementById('nav-wrapper');
    var hamburger = document.getElementById('js-hamburger');
    var blackBg = document.getElementById('js-black-bg');

    hamburger.addEventListener('click', function () {
        nav.classList.toggle('open');
    });
    blackBg.addEventListener('click', function () {
        nav.classList.remove('open');
    });
};


// 写真の切り替え
$(function(){
    // 初期画像の表示
    let index = 0;
    $('.img').eq(index).addClass('current-img');
    
    setInterval(function(){
      // 非表示
      $('.img').eq(index).removeClass('current-img');
      // 画像の最後判定
      if(index == $('.img').length - 1){
        index = 0;
      }else{
        index++;
      }
      // 表示
      $('.img').eq(index).addClass('current-img');
    }, 5000);
  });