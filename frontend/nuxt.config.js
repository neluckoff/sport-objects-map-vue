export default {
  // target: 'static',
  ssr: true,
  loading: true,
  server: {
    host: process.env.HOST || '0.0.0.0',
    port: process.env.PORT || 3000
  },

  head: {
    title: 'Карта Спорта',
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
    ['@nuxtjs/style-resources'],
    ['@nuxtjs/axios'],
    ['@nuxtjs/pwa'],
    ['nuxt-leaflet'],
  ],

  axios: {
    prefix: '/api/',
        proxy: true,
  },

  proxy: {
    '/api': {
        target: 'http://backend:8010',
        pathRewrite: {'^/api/': ''},
        headers: { 'X-API-KEY': 'apiKey' },
    },
  },

  pwa: {
    meta: {
        title: 'Карта Спорта',
        author: 'luckoff',
    },
    manifest: {
        name: 'Карта Спорта',
        short_name: 'Карта Спорта',
        lang: 'ru',
    },
  },

  build: {
  }
}
