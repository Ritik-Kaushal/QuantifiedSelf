<template>
  <div>
    <!-- Trigger for Update Details Modal -->
    <div class="mt-2">
      <button
        type="button"
        class="btn btn-primary"
        data-bs-toggle="modal"
        :data-bs-target="'#' + modal_id"
      >
        Update Details
      </button>
    </div>
    <!-- Trigger for Update Details Modal -->

    <!-- Update Details Modal -->
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
            <h5 class="modal-title" id="staticBackdropLabel">Update Details</h5>
          </div>
          <div class="modal-body">
            <div class="alert alert-danger" role="alert" v-if="error">
              {{ error_msg }}
            </div>

            <form>
              <div class="input-group mb-3">
                <span class="input-group-text" id="inputGroup-sizing-default"
                  >Tracker Name
                </span>
                <input
                  type="text"
                  class="form-control"
                  aria-label="Sizing example input"
                  aria-describedby="inputGroup-sizing-default"
                  name="tracker_name"
                  :value="$store.getters.get_selected_tracker.tracker_name"
                  disabled
                  readonly
                />
              </div>
              <div class="input-group mb-3">
                <span class="input-group-text" id="inputGroup-sizing-default"
                  >Tracker Type
                </span>
                <input
                  type="text"
                  class="form-control"
                  aria-label="Sizing example input"
                  aria-describedby="inputGroup-sizing-default"
                  name="tracker_type"
                  :value="$store.getters.get_selected_tracker.tracker_type"
                  disabled
                  readonly
                />
              </div>
              <div class="input-group mb-3">
                <span class="input-group-text" id="inputGroup-sizing-default"
                  >Timestamp</span
                >
                <input
                  class="form-control"
                  type="text"
                  name="time_stamp"
                  v-model="time_stamp"
                  aria-label="Disabled input example"
                />
              </div>
              <div class="input-group mb-3">
                <span class="input-group-text" id="inputGroup-sizing-default"
                  >Value</span
                >
                <input
                  type="text"
                  class="form-control"
                  aria-label="Sizing example input"
                  aria-describedby="inputGroup-sizing-default"
                  name="value"
                  v-model="value"
                />
              </div>

              <div class="input-group mb-3">
                <span class="input-group-text" id="inputGroup-sizing-default"
                  >Note</span
                >
                <input
                  type="text"
                  class="form-control"
                  aria-label="Sizing example input"
                  aria-describedby="inputGroup-sizing-default"
                  name="note"
                  v-model="note"
                />
              </div>
              <div class="modal-footer">
                <button class="btn btn-primary" @click="updateLog($event)">
                  Update
                </button>
                <button
                  type="button"
                  class="btn btn-secondary"
                  data-bs-dismiss="modal"
                >
                  Cancel
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- Update Details Modal -->
</template>

<script>
import FetchFunction from "@/utils";
export default {
  name: "UpdateTrackerModal",
  props: ["modal_id", "log"],
  mounted() {
    (this.error = false), (this.error_msg = ""), (this.value = this.log.value);
    this.note = this.log.note;
    this.time_stamp = this.log.time_stamp;
  },
  data() {
    return {
      error: false,
      error_msg: "",
      value: "",
      note: "",
      time_stamp: "",
    };
  },
  methods: {
    async updateLog(e) {
      e.preventDefault();
      let data = {
        log_id: this.log.id,
        value: this.value,
        note: this.note,
        time_stamp: this.time_stamp,
      };

      console.log(data);
      let url = "http://localhost:5000/api/trackerLogs/put";
      let init_obj = {
        method: "PUT",
        mode: "cors",
        body: JSON.stringify(data),
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
          console.log("here done")
          await this.$store.dispatch("getLogs")
          await this.$store.dispatch("getDataSummary");

        })
        .catch((e) => {
          this.error_msg = e.message;
          this.error = true;
          const err = JSON.parse(e.message);

            if (err.error_code == "TIM" || err.error_code == "IVT") {
              this.$store.dispatch('logoutUser');

            }
        }).catch();
    },
  },
};
</script>
