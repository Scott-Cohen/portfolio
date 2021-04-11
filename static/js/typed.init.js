// index-startup-business.html
if(document.getElementsByClassName('typed-business').length > 0) {
    var typed = new Typed('.typed-business', {
        stringsElement: '#typed-strings',
        typeSpeed: 200,
        loop: true,
        strings: [
            'Develop', 'Growing', 'We Build',
        ],
    });
}