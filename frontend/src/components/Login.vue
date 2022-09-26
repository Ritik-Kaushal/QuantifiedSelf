<template>
  <div class="login-part" ref="scroll" >
    <form>
      <p class="login-header">Please login to your account</p>

      <div class="form-outline mb-4 input-part">
        <input
          type="email"
          class="form-control"
          placeholder="Email address"
          v-model="email"
        />
      </div>

      <div class="form-outline mb-4 input-part">
        <input
          type="password"
          class="form-control"
          placeholder="Password"
          v-model="password"
        />
      </div>

      <div class="text-center pt-1 mb-5 pb-1">
        <button
          @click="login($event)"
          class="btn btn-primary btn-block fa-lg gradient-custom-2 mb-3"
          type="button"
        >
          Log in
        </button>
        <br />
        <a class="text-muted" href="#!">Forgot password?</a>
      </div>

      <div
        class="d-grid align-items-center justify-content-center pb-4"
        id="custom-create-part"
      >
        <p class="mb-0 me-2">Don't have an account?</p>

        <button type="button" class="btn btn-outline-danger">
          <router-link @click.native="addClass" to="/home/register"
            >Register</router-link
          >
        </button>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: "LOGIN",
  mounted() {
    this.$refs["scroll"].scrollIntoView();
  },
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    login(e) {
      e.preventDefault();
      console.log(this.email);
      console.log(this.password);
    },
  },
};
</script>

<style scoped>
.login-part {
  display: flex;
  position: relative;

  justify-content: center;
  align-items: center;
  margin-left: 0;
}
.input-part {
  display: flex;
  justify-content: center;
  align-items: center;
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
</style>
