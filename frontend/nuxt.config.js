export default {
  target: 'static',
  ssr: true,
  loading: true,

  head: {
    title: 'yandex-map',
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
    // { src: '~plugins/leaflet.js', mode: 'client' },
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
    ['nuxt-leaflet']
  ],

  axios: {
    prefix: '/api/v1/',
        proxy: true,
  },

  proxy: {
    '/api/v1': {
        target: 'http://localhost:8010',
        secure: false,
        headers: { 'X-API-KEY': 'apiKey' },
        //logLevel: 'debug',
    },
  },

  pwa: {
    meta: {
        title: 'ЦРК МИРЭА',
        author: 'luckoff',
        // theme_color: '#f3f3f3',
    },
    manifest: {
        name: 'ЦРК МИРЭА',
        short_name: 'ЦРК МИРЭА',
        lang: 'ru',
    },
  },

  build: {
  }
}
