<template lang="pug">
  v-container
    v-layout.text-xs-center(align-center justify-center row)
      v-flex.theme--light.application(xs4)
        v-container.text-xs-center(style="position: relative;top: 13%;")
          v-card(flat)
            v-card-title(primary-title)
              h4 Авторизация
            v-form(@submit.prevent="auth()")
              p(v-if="errors.non_field_errors" style="color: red") {{ errors['non_field_errors'] }}
              v-text-field(prepend-icon="person" name="username" label="Username" v-model="user.username" required :error-messages="errors.username" @keyup="errors.username = ''")
              v-text-field(prepend-icon="lock" name="password" label="Password" type="password" v-model="user.password" required :error-messages="errors.password" @keyup="errors.password = ''")
              v-card-actions
                v-btn(color="info" large block type="submit") Авторизоваться
</template>

<script>
import Api from '../services/api'
export default {
  name: "Login",
  data() {
    return {
      user: {
        username: '',
        password: '',
      },
      errors: {
        'non_field_errors': '',
        'username': '',
        'password': '',
      },
    }
  },
  methods: {
    auth: function () {
      Api().post('/auth/login/', this.user)
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

