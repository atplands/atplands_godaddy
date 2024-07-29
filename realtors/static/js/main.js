const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();



$('.list_slider').owlCarousel({
    loop:true,
    margin:10,
    nav: false,
    loop: true,
    mouseDrag: true,
    responsiveClass: true,
    navText: ["<i class='icofont-bubble-left'></i>", "<i class='icofont-bubble-right'></i>"],
    dots:true,
    responsive:{
        0:{
            items:1.15
        },

        1000:{
            items:3
        }
    }
});

$('.agri_l').owlCarousel({
    loop:true,
    margin:10,
    nav: false,
    loop: true,
    mouseDrag: true,
    responsiveClass: true,
    navText: ["<i class='icofont-bubble-left'></i>", "<i class='icofont-bubble-right'></i>"],
    dots:true,
    responsive:{
        0:{
            items:1.15
        },

        1000:{
            items:4.15
        }
    }
});

$('.venture_p').owlCarousel({
    loop:true,
    margin:10,
    nav: false,
    loop: true,
    mouseDrag: true,
    responsiveClass: true,
    navText: ["<i class='icofont-bubble-left'></i>", "<i class='icofont-bubble-right'></i>"],
    dots:true,
    responsive:{
        0:{
            items:1.15
        },

        1000:{
            items:4.15
        }
    }
});

$('.comm_l').owlCarousel({
    loop:true,
    margin:10,
    nav: false,
    loop: true,
    mouseDrag: true,
    responsiveClass: true,
    navText: ["<i class='icofont-bubble-left'></i>", "<i class='icofont-bubble-right'></i>"],
    dots:true,
    responsive:{
        0:{
            items:1.15
        },

        1000:{
            items:4.15
        }
    }
});

$('.farm_h').owlCarousel({
    loop:true,
    margin:10,
    nav: false,
    loop: true,
    mouseDrag: true,
    responsiveClass: true,
    navText: ["<i class='icofont-bubble-left'></i>", "<i class='icofont-bubble-right'></i>"],
    dots:true,
    responsive:{
        0:{
            items:1.15
        },

        1000:{
            items:4.15
        }
    }
});

$('.house_r').owlCarousel({
    loop:true,
    margin:10,
    nav: false,
    loop: true,
    mouseDrag: true,
    responsiveClass: true,
    navText: ["<i class='icofont-bubble-left'></i>", "<i class='icofont-bubble-right'></i>"],
    dots:true,
    responsive:{
        0:{
            items:1.15
        },

        1000:{
            items:4.15
        }
    }
});

$(".owl-carousel").owlCarousel({
    // you can use jQuery selector
    navText: [$('.swiper-button-next'),$('.swiper-button-prev')]

});

/*scrolling banner*/
(function ($) {
  "use strict";

  $(document).ready(function () {
    $(".lease_l").owlCarousel({
      items: 4,
      nav: false,
      loop: true,
      dots: true,
      mouseDrag: true,
      responsiveClass: true,
      navText : ["<i class='fas fa-long-arrow-alt-left'></i>","<i class='fas fa-long-arrow-alt-right'></i>"],
      responsive: {
        0: {
          items: 1.15,
        },
        480: {
          items: 1.15,
        },
        767: {
          items: 1.25,
        },
        992: {
          items: 4.25,
        },
        1200: {
          items: 4.25,
        },
      },
    });
  });

  $(document).ready(function () {
    $(".land_p").owlCarousel({
      items: 4,
      nav: false,
      loop: true,

      mouseDrag: true,
      responsiveClass: true,
      navText: ["<i class='icofont-bubble-left'></i>", "<i class='icofont-bubble-right'></i>"],
      responsive: {
        0: {
          items: 1.15,
        },
        480: {
          items: 1.15,
        },
        767: {
          items: 3.15,
        },
        992: {
          items: 4.15,
        },
        1200: {
          items: 4.15,
        },
      },
    });
  });

  $(document).ready(function () {
    $(".house_r").owlCarousel({
      items: 4,
      nav: false,
      dots: true,
      loop: true,
      margin:10,
      mouseDrag: true,
      responsiveClass: true,
      autoplay: true,
      autoplayTimeout: 3000,
      autoplayHoverPause: true,
      navText: ["<i class='icofont-scroll-left'></i>", "<i class='icofont-scroll-right'></i>"],
      responsive: {
        0: {
          items: 1.15,
        },
        480: {
          items: 1.15,
        },
        767: {
          items: 3.15,
        },
        992: {
          items: 4.15,
        },
        1200: {
          items: 4.15,
        },
      },
    });
  });
})(jQuery);

<!--Start of Tawk.to Script-->
<!--script type="text/javascript"-->
var Tawk_API=Tawk_API||{}, Tawk_LoadStart=new Date();
(function(){
var s1=document.createElement("script"),s0=document.getElementsByTagName("script")[0];
s1.async=true;
s1.src='https://embed.tawk.to/6203e072b9e4e21181be43af/1frfi9h1r';
s1.charset='UTF-8';
s1.setAttribute('crossorigin','*');
s0.parentNode.insertBefore(s1,s0);
})();
<!--/script-->
<!--End of Tawk.to Script-->


