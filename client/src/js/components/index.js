import Login from './Login'
import Register from './Register'
import AppList from './AppList'

export default function components(Vue) {
  Vue.component('app-list', AppList)
  Vue.component('login-form', Login)
  Vue.component('register-form', Register)
}
