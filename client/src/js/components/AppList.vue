<template lang="pug">
  div
    v-toolbar(flat, color="white")
      v-toolbar-title My applications
      v-divider.mx-2(inset, vertical)
      v-spacer
      v-dialog(v-model="dialog" max-width="500px")
        v-btn.mb-2(slot="activator", color="primary", dark) New App
        v-card
          v-card-title
            span.headline {{ formTitle }}
          v-card-text
            v-container(grid-list-md)
              v-layout(wrap)
                v-flex(xs12, sm6, md4)
                  v-text-field(v-model="editedItem.name" label="Application name" required :error-messages="errors.name" @keyup="errors.name = ''")
                v-flex(xs12, sm6, md4)
                  v-text-field(v-model="editedItem.hook_url" label="Hook URL" required :error-messages="errors.hook_url" @keyup="errors.hook_url = ''")
                v-flex(xs12, sm6, md4)
                  v-text-field(v-model="editedItem.style_url" label="Style URL" required :error-messages="errors.style_url" @keyup="errors.style_url = ''")
          v-card-actions
            v-spacer
            v-btn(color="blue darken-1", flat, @click="close") Cancel
            v-btn(color="blue darken-1", flat, @click="save") Save

    v-data-table.elevation-1(:headers="headers", :items="items")
      template(slot="items", slot-scope="props")
        td {{ props.item.name }}
        td
          v-text-field(readonly :value="props.item.hook_url" style="font-size: 11px !important;")
        td
          v-text-field(readonly :value="props.item.style_url" style="font-size: 11px !important;")
        td
          v-text-field(readonly :value="props.item.token" style="font-size: 13px !important;")
        td.fill-height.px-0
          v-layout.justify-center
            v-icon.mr-2(small, @click="generateToken(props.item)") replay
            v-icon.mr-2(small, @click="editItem(props.item)") edit
            v-icon.mr-2(small, @click="deleteItem(props.item.id)") delete
      template(slot="no-data")
        v-btn(color="primary" @click="fetchData") Reset
    code(style="margin-top: 25px;")
      |{
      |    "token": "token",
      |    "height": 100000,
      |    "width": 1920,
      |    "pages": [
      |        {
      |            "post_type": "",
      |            "term_id": "",
      |            "post_id": "",
      |            "url": "https://website.url/"
      |        }
      |    ]
      |}
</template>

<script>
import Api from './../services/api'
export default {
  name: "AppList",
  data() {
    return {
      dialog: false,
      items: [],
      headers: [
        {text: 'Application name', align: 'left', sortable: false, value: 'name'},
        {text: 'Hook URL', align: 'left', sortable: false, value: 'hook_url'},
        {text: 'Style URL', align: 'left', sortable: false, value: 'style_url'},
        {text: 'Token', align: 'left', sortable: false, value: 'token'},
        {text: 'Actions', value: 'name', sortable: false}
      ],
      errors: {
        name: '',
        hook_url: '',
        style_url: ''
      },
      defaultItem: {
        name: '',
        hook_url: '',
        style_url: '',
      },
      editedItem: {
        name: '',
        hook_url: '',
        style_url: '',
      }
    }
  },
  computed: {
    formTitle () {
      return this.editedIndex === -1 ? 'New application' : 'Edit application'
    }
  },
  watch: {
    dialog (val) {
      val || this.close()
    }
  },
  created () {
    this.fetchData()
  },
  methods: {
    fetchData: function () {
      Api().get('/api/v1/apps/')
        .then((response) => {
          this.items = response.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    generateToken: function (item) {
      Api().put(`/api/v1/apps/${item.id}/regenerate_token/`)
        .then(() => {
          this.fetchData()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    editItem: function (item) {
      this.editedIndex = this.items.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialog = true
    },
    deleteItem: function (id) {
      Api().delete(`/api/v1/apps/${id}/`)
        .then(() => {
          this.fetchData()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    close: function () {
      this.dialog = false
      setTimeout(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      }, 300)
    },
    save: function () {
      if (this.editedIndex > -1) {
        let data = {
          name: this.editedItem.name,
          hook_url: this.editedItem.hook_url,
          style_url: this.editedItem.style_url
        }
        Api().patch(`/api/v1/apps/${this.editedItem.id}/`, data)
          .then(() => {
            this.fetchData()
            this.close()
          })
          .catch((error) => {
            for (let field in error.response['data']) {
              this.errors[field] = error.response['data'][field][0]
            }
          })
      } else {
        Api().post('/api/v1/apps/', this.editedItem)
          .then(() => {
            this.fetchData()
            this.close()
          })
          .catch((error) => {
            for (let field in error.response['data']) {
              this.errors[field] = error.response['data'][field][0]
            }
          })
      }
    }
  }
}
</script>
