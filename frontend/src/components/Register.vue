<template>
  <div class="register-part" ref="scroll">
    <form>
      <p class="register-header">Create an Account</p>

      <div class="form-outline mb-4 input-part">
        <input
          type="text"
          class="form-control"
          placeholder="Name"
          v-model="name"
        />
      </div>
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
          type="tel"
          class="form-control"
          placeholder="Phone Number"
          v-model="phone_no"
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

      <div class="form-outline mb-4 input-part">
        <input
          type="password"
          class="form-control"
          placeholder="Re-enter Password"
          v-model="re_password"
        />
      </div>

      <div class="text-center pt-1 mb-5 pb-1">
        <button
          @click="register($event)"
          class="btn btn-primary btn-block fa-lg gradient-custom-2 mb-3"
          type="button"
        >
          Create Account
        </button>
        <br />
      </div>
      <div
        class="d-grid align-items-center justify-content-center pb-4"
        id="custom-create-part"
      >
        <p class="mb-0 me-2">Already have an account?</p>
        <button type="button" class="btn btn-outline-danger">
          <router-link @click.native="addClass" to="/home/login"
            >Login</router-link
          >
        </button>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: "REGISTER",
  mounted() {
    this.$refs["scroll"].scrollIntoView();
  },
  data() {
    return {
      email: "",
      password: "",
      re_password: "",
      name: "",
      phone_no: "",
    };
  },
  methods: {
    register(e) {
      e.preventDefault();
      e.preventDefault();
      console.log(this.email);
      console.log(this.password);
      console.log(this.re_password);
      console.log(this.name);
      console.log(this.phone_no);
    },
  },
};
</script>

<style scoped>
.register-part {
  display: flex;
  position: relative;

  justify-content: center;
  align-items: center;
}
.register-part {
  display: flex;
  justify-content: center;
  align-items: center;
}
.register-header {
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
