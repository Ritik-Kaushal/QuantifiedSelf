<template>
  <div>
    <!-- Trigger for Delete Modal -->
    <div class="mt-2">
      <button
        type="button"
        class="btn btn-primary"
        data-bs-toggle="modal"
        :data-bs-target="'#' + modal_id"
      >
        Delete
      </button>
    </div>
    <!-- Trigger for Delete Modal -->

    <!-- Delete Modal -->
    <div
      class="modal fade"
      :id="modal_id"
      data-bs-backdrop="static"
      data-bs-keyboard="false"
      tabindex="-1"
      aria-labelledby="staticBackdropLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
        <div class="modal-content">
          <div class="modal-header justify-content-center">
            <h5 class="modal-title" id="staticBackdropLabel">
              Do you want to Delete this Log
            </h5>
          </div>
          <div class="modal-body">
            <div class="alert alert-danger" role="alert" v-if="error">
              {{ error_msg }}
            </div>
            <form>
              <div class="mb-3 form-check">
                <input
                  type="checkbox"
                  class="form-check-input"
                  name="check_point"
                  id="check_point"
                  v-model="what_to_do"
                />
                <label class="form-check-label" for="check_point"
                  >Do you really want to delete this log ?</label
                >
              </div>
              <div class="modal-footer">
                <button class="btn btn-primary" @click="deleteLog($event)">
                  Yes
                </button>
                <button
                  type="button"
                  class="btn btn-secondary"
                  data-bs-dismiss="modal"
                >
                  No
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
    <!-- Delete Modal -->
  </div>
</template>

<script>
import FetchFunction from "@/utils";
export default {
  name: "DeleteTrackerModal",
  props: ["modal_id", "log_id"],
  data() {
    return {
      error: false,
      error_msg: "",
      what_to_do: false,
    };
  },
  methods: {
    async deleteLog(e) {
      console.log(this.log_id);
      e.preventDefault();
      if (this.what_to_do) {
        let url =
          "http://localhost:5000/api/trackerLogs/delete?log_id=" + this.log_id;
        let init_obj = {
          method: "DELETE",
          mode: "cors",
          headers: {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
          },
        };

        let res = await FetchFunction({
          url: url,
          init_obj: init_obj,
          authRequired: true,
        })
          .then(async (d) => {
            var par = "#" + this.modal_id;
            $(par).modal("hide");
            await this.$store.dispatch("getLogs");
            await this.$store.dispatch('getDataSummary');
          })
          .catch((e) => {
            
            this.error_msg = e.message;
            this.error = true;
            
            const err = JSON.parse(e.message);
            if (err.error_code == "TIM" || err.error_code == "IVT") {
              this.$store.dispatch('logoutUser');

            }
          }).catch();
      } else {
        this.error_msg = "Please check the checkbox to delete";
        this.error = true;
      }
    },
  },
};
</script>
