export default {
  target: 'static',
  ssr: true,
  loading: true,

  head: {
    title: 'Sport Objects Map',
    htmlAttrs: {
      lang: 'ru'
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },

  css: [
    '@/assets/scss/index.scss',
  ],

  styleResources: {
    sass: [],
    scss: [
        '@/assets/scss/_base/_variables.scss',
        '@/assets/scss/_mixins/*.scss',
    ],
    less: [],
  },

  plugins: [
    { src: '~plugins/leaflet.js', mode: 'client' },
    { src: '~plugins/chart.js', mode: 'client' },
  ],

  components: true,

  buildModules: [
    // '@nuxtjs/eslint-module'
    ["@nuxtjs/svg"],
    ['@nuxtjs/pwa'],
    ['@nuxtjs/moment'],
  ],

  moment: {
    defaultTimezone: 'Europe/Moscow',
    locales: ['ru'],
    defaultLocale: 'ru'
  },

  modules: [
    ['@nuxtjs/axios'],
    ['@nuxtjs/pwa'],
    ['nuxt-leaflet'],
    // ['vue2-leaflet-markercluster']
  ],

  axios: {
    prefix: '/api',
        proxy: true,
  },

  proxy: {
    '/api': {
        target: 'http://localhost:8010',
        pathRewrite: {'^/api/': ''},
        headers: { 'X-API-KEY': 'apiKey' },
        //logLevel: 'debug',
    },
  },

  pwa: {
    meta: {
        title: 'Sport Objects Map',
        author: 'luckoff',
        // theme_color: '#f3f3f3',
    },
    manifest: {
        name: 'Sport Objects Map',
        short_name: 'Sport Objects Map',
        lang: 'ru',
    },
  },

  build: {
  }
}
