<template>
  <div>
    <div class="accordion" id="accordionExample">
      <div class="accordion-item">
        <h2 class="accordion-header" id="headingOne">
          <button
            class="accordion-button"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#collapseOne"
            aria-expanded="true"
            aria-controls="collapseOne"
          >
            <strong class="fs-5">Edit Name</strong>
          </button>
        </h2>
        <div
          id="collapseOne"
          class="accordion-collapse collapse show"
          aria-labelledby="headingOne"
          data-bs-parent="#accordionExample"
        >
          <div class="accordion-body">
            <div>
              <svg xmlns="http://www.w3.org/2000/svg" style="display: none">
                <symbol
                  id="exclamation-triangle-fill"
                  fill="currentColor"
                  viewBox="0 0 16 16"
                >
                  <path
                    d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"
                  />
                </symbol>
              </svg>
              <div
                class="alert alert-danger d-flex align-items-center"
                role="alert"
              >
                <svg
                  class="bi flex-shrink-0 me-2"
                  width="24"
                  height="24"
                  role="img"
                  aria-label="Danger:"
                >
                  <use xlink:href="#exclamation-triangle-fill" />
                </svg>
                <div>
                </div>
              </div>
            </div>
            <form method="POST" , action="/edit_profile">
              <input type="hidden" name="edit_what" value="name" />
              <div class="input-group mb-3">
                <span class="input-group-text" id="basic-addon1">Name</span>
                <input
                  type="text"
                  class="form-control"
                  placeholder="Name"
                  aria-label="Name"
                  aria-describedby="basic-addon1"
                  name="name"
                />
              </div>
              <div>
                <button type="submit" class="btn btn-warning">Update</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
    Update Details
  </div>
</template>
<script>
export default {
  name: "updateDetails",
  mounted() {
    this.$store.commit("change_active", 3);
  },
};
</script>
