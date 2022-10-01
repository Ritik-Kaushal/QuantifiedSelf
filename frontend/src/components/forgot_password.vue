<template>
  <div class="reset-part" ref="scroll">
    <div v-if="loading">
      <p class="reset-part"><strong>Sending the email... Please Wait</strong></p>
    </div>
    <div v-else>
      <form>
        <p class="reset-header"><strong>Enter your email</strong></p>
        <div class="alert alert-danger error" role="alert" v-if="api_error">
          {{ error_message }}
        </div>
        <div class="form-outline mb-4 input-part">
          <input
            type="email"
            class="form-control"
            placeholder="Email address"
            v-model="email"
          />
          <span class="error" v-if="email_error">Email is required !!!</span>
        </div>
        <div class="text-center pt-1 mb-5 pb-1">
          <button
            @click="reset($event)"
            class="btn btn-primary btn-block fa-lg gradient-custom-2 mb-3"
            type="button"
            id="reset_button"
          >
            Reset
          </button>
          <br />
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import FetchFunction from "@/utils";
export default {
  name: "ForgotPassword",
  mounted() {
    if (this.$store.getters.get_login_status) {
      this.$router.push({ name: "Dashboard" });
    }
    this.$refs["scroll"].scrollIntoView();
  },
  data() {
    return {
      loading: false,
      email: "",
      email_error: false,
      api_error: false,
      error_msg: "",
    };
  },
  watch: {
    email() {
      if (this.email.trim() == "") {
        this.email_error = true;
        document.getElementById("reset_button").disabled = true;
      } else {
        this.email_error = false;
        document.getElementById("reset_button").disabled = false;
      }
    },
  },
  methods: {
    async reset(e) {
      this.loading = true;
      e.preventDefault();
      const user_email = { email: this.email };
      const res = await FetchFunction({
        url: "http://127.0.0.1:5000/reset",
        init_obj: {
          headers: {
            "Content-Type": "application/json",
          },
          method: "POST",
          body: JSON.stringify(user_email),
        },
      })
        .then((data) => {
          alert("Reset mail has been sent. Please check your email.");
          this.loading = false;
          this.$router.push({ path: "/home/login" });
        })
        .catch((err) => {
          this.loading = false;
          err = JSON.parse(err.message);
            this.error_message = err.response.errors[0];
            this.api_error = true;
        })
        .catch((e) => {
            console.log(e);
        });
    },
  },
};
</script>

<style scoped>
  .login-part {
    display: grid;
    position: relative;
  
    justify-content: center;
    align-items: center;
  }
  .input-part {
    display: grid;
  }
  .login-header {
    margin-top: 2rem;
    font-weight: 500;
    margin: 2rem auto;
    text-align: center;
  }
  a {
    text-decoration: none;
    color: black;
  }
  .error {
    align-items: center;
    justify-content: center;
    width: 100%;
    color: red;
  }
  .alert {
    padding-top: 4px;
    padding-bottom: 4px;
  }
  </style>