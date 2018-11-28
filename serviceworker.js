var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
    '/',
    '/accounts/login/',
    'registro/',
    'registroMascotas/',
    '/static/core/css/estilos.css',
    '/static/core/img/crowfunding.jpg',
    '/static/core/img/icoMisPerris.png',
    '/static/core/img/logo.png',
    '/static/core/img/adoptados/perro.png',
    '/static/core/img/adoptados/Apolo.jpg',
    '/static/core/img/adoptados/Duque.jpg',
    '/static/core/img/adoptados/Tom.jpg',
    '/static/core/img/rescatados/Bigotes.jpg',
    '/static/core/img/rescatados/Chocolate.jpg',
    '/static/core/img/rescatados/Luna.jpg',
    '/static/core/img/rescatados/Maya.jpg',
    '/static/core/img/rescatados/Oso.jpg',
    '/static/core/img/rescatados/Pexel.jpg',
    '/static/core/img/rescatados/Wifi.jpg',
    '/static/core/img/rescate.jpg',
    '/static/core/img/Social-mail.png',
    '/static/core/img/social-inst.png',
    '/static/core/img/social-twitter.png',
    '/static/core/img/socialfacebook.png',
    '/static/core/img/socialplus.png',
    'https://cdn.jsdelivr.net/bxslider/4.2.12/jquery.bxslider.css',
    'https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js',
    'https://cdn.jsdelivr.net/bxslider/4.2.12/jquery.bxslider.min.js',
    '/static/core/js/inicializacion.js'
];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', function(event){
    event.respondWith(
        caches.match(event.request).then(function(response) {
            return fetch(event.request).catch(function() {
                return response;
            })
        })
    );
});