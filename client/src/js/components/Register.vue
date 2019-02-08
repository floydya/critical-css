<template lang="pug">
  v-layout.text-xs-center(align-center justify-center row)
    v-flex.theme--light.application(xs4)
      v-container.text-xs-center(style="position: relative;top: 13%;")
        v-card(flat)
          v-card-title(primary-title)
            h4 Регистрация
          v-form(@submit.prevent="register()")
            p(v-if="errors.non_field_errors" style="color: red") {{ errors['non_field_errors'] }}
            v-text-field(prepend-icon="person" name="username" label="Username" v-model="user.username" required :error-messages="errors.username" @keyup="errors.username = ''")
            v-text-field(prepend-icon="email" name="email" label="Email" type="email" v-model="user.email" required :error-messages="errors.email" @keyup="errors.email = ''")
            v-text-field(prepend-icon="lock" name="password" label="Password" type="password" v-model="user.password" required :error-messages="errors.password" @keyup="errors.password = ''")
            v-text-field(prepend-icon="lock" name="confirm_password" label="Password" type="password" v-model="user.confirm_password" required :error-messages="errors.confirm_password" @keyup="errors.confirm_password = ''")
            v-card-actions
              v-btn(color="info" large block type="submit") Зарегистрироваться
</template>

<script>
import Api from '../services/api'
export default {
  name: "Register",
  data() {
    return {
      user: {
        username: '',
        email: '',
        password: '',
        confirm_password: ''
      },
      errors: {
        non_field_errors: '',
        username: '',
        email: '',
        password: '',
        confirm_password: ''
      },
    }
  },
  methods: {
    register: function () {
      Api().post('/auth/register/', this.user)
        .then(() => {
          window.location.href = '/'
        })
        .catch((error) => {
          for (let field in error.response['data']) {
            this.errors[field] = error.response['data'][field][0]
          }
        })
    }
  }
}
</script>
