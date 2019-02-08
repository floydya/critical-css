import Vue from 'vue'
import Vuetify from 'vuetify'

import components from './components'
Vue.use(components)
Vue.use(Vuetify)

window.app = new Vue({
  el: '#app'
})
