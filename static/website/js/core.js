$(document).on('click', 'a[href^="#"]', function (event) {
    event.preventDefault();

    $('html, body').animate({
        scrollTop: $($.attr(this, 'href')).offset().top - 130
    }, 500);
});
$(function () {
   
    ActiveSlide();
    GetTodayYear();
    DirectionsModalAddText();
    PopoverProjects();
    UpToHome();
    var header = $(".header");
    var headerlogo = $(".header_logo");

    var sticky = header[0].offsetTop;

    window.onscroll = function () { ResizeHeaderImg() };

    function ResizeHeaderImg() {
        if (window.pageYOffset > sticky) {
            headerlogo.addClass("header_logo__sm");
        } else {
            headerlogo.removeClass("header_logo__sm");
        }
    }
    $("#clients-slider").lightSlider({
        item: 5,
        loop: true,
        slideMove: 3,
        slideMargin: 17,
        speed: 600,
        pager: false,
        adaptiveHeight: false,
        prevHtml: "<span class=\"ico_prev\"></span>",
        nextHtml: "<span class=\"ico_next\"></span>",
        responsive: [
            {
                breakpoint: 800,
                settings: {
                    item: 5,
                    slideMove: 3,
                    slideMargin: 6,
                }
            },
            {
                breakpoint: 480,
                settings: {
                    item: 2,
                    slideMove: 1
                }
            }
        ]
    });
    $(".projects_img").hover(function () {
    });

    $('#lic-gallery').lightGallery({
        selector: '.gallery-selector',
        thumbnail: true,
        animateThumb: false,
        showThumbByDefault: false
    });
});
function PopoverProjects(text) {
    $('.projects_popover').popover({
        container: 'body',
        html: true,
        title: function () {
            return $(this).parent().find(".projects_title").html();
        },
        content: function () {
            return '<div class="projects_popover-content">' + $(this).parent().find(".projects_content").html() + '</div>'
                + '<div class="text-center"><button type="button" class="btn btn-primary btn-lg btn-to-offer" data-toggle="modal" data-target="#offersModal">Заказать расчет подобного проекта</button></div>';
        }
    });
}
function DirectionsModalAddText() {
    $(".directions_link").click(function () {

        $("#directionsModal").find(".modal-header").find(".modal-title").empty();
        $("#directionsModal").find(".modal-body").find(".directions_description").empty();

        var text = $(this).parent().find(".directions_description").html();
        var title = $(this).parent().find(".directions_title").html();
      
        $("#directionsModal").find(".modal-header").find(".modal-title").append(title);
        $("#directionsModal").find(".modal-body").find(".directions_description").append(text);
    });

    $(".projects_link").click(function () {

        $("#projectsInfo").find(".modal-header").find(".modal-title").empty();
        $("#projectsInfo").find(".modal-body").find(".projects_description").empty();

        var imgSrc = $(this).parent().find(".projects_img").attr("src");
        var text = $(this).parent().find(".projects_content").html();
        var title = $(this).parent().find(".projects_title").html();

        $("#projectsInfo").find(".modal-header").find(".modal-title").append(title);
        $("#projectsInfo").find(".modal-body").find(".projects_description").append(text);
        $("#projectsInfo").find(".modal-body").find(".projects_img").attr("src", imgSrc);
    });
}
function GetTodayYear() {
    var date = new Date();
    $(".nowadays-year").text(date.getFullYear());
}
function UpToHome() {
    var top_show = 150; // В каком положении полосы прокрутки начинать показ кнопки "Наверх"
    var delay =750; // Задержка прокрутки
        $(window).scroll(function () { // При прокрутке попадаем в эту функцию
            /* В зависимости от положения полосы прокрукти и значения top_show, скрываем или открываем кнопку "Наверх" */
            if ($(this).scrollTop() > top_show) $('#top').fadeIn();
            else $('#top').fadeOut();
        });
        $('#top, #logo_up').click(function () { // При клике по кнопке "Наверх" попадаем в эту функцию
            /* Плавная прокрутка наверх */
            $('body, html').animate({
                scrollTop: 0
            }, delay);
        });
}
function DisplayErrors(errors) {
    var c = "";
    for (var prop in errors) { 
        if ((errors[prop]).length!=0)
        c += (errors[prop])[0] + "<br>";
    }
    return c;
}
function ActiveSlide() {
    var str = $("#content").attr("data-t");
    var sliderItems = $(".carousel-item");
    var k = 0;
    $(sliderItems).each(function () {
        if ($(this).attr("data-t") == str) {
            $(this).addClass("active")
            k++;
        }
        else
            $(this).removeClass("active");
    });
    if (k == 0)
        sliderItems.first().addClass("active");
}
