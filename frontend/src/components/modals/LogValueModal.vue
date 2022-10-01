<template>
  <div>
    <!-- Trigger for Log a value Modal -->
    <div>
      <button
        type="button"
        class="btn btn-primary"
        data-bs-toggle="modal"
        data-bs-target="#logValueModal"
        @click="generateTimestamp($event)"
      >
        Log a value
      </button>
    </div>
    <!-- Trigger for Log a value Modal -->

    <!-- Log a value Modal -->
    <div
      class="modal fade"
      id="logValueModal"
      data-bs-backdrop="static"
      data-bs-keyboard="false"
      tabindex="-1"
      aria-labelledby="staticBackdropLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
        <div class="modal-content">
          <div class="modal-header justify-content-center">
            <h5 class="modal-title" id="staticBackdropLabel">Log a value</h5>
          </div>
          <div class="modal-body">
            <div class="alert alert-danger" role="alert" v-if="error">
              {{ error_msg }}
            </div>
            <form>
              <div class="input-group mb-3">
                <span class="input-group-text" id="inputGroup-sizing-default"
                  >Tracker Name</span
                >
                <input
                  type="text"
                  class="form-control"
                  aria-label="Sizing example input"
                  aria-describedby="inputGroup-sizing-default"
                  name="tracker_name"
                  :value="this.$store.getters.get_selected_tracker.tracker_name"
                  disabled
                  readonly
                />
              </div>
              <div class="input-group mb-3">
                <span class="input-group-text" id="inputGroup-sizing-default"
                  >Tracker Type</span
                >
                <input
                  class="form-control"
                  type="text"
                  name="tracker_type"
                  :value="this.$store.getters.get_selected_tracker.tracker_type"
                  aria-label="Disabled input example"
                  disabled
                  readonly
                />
              </div>
              <div class="input-group mb-3">
                <span class="input-group-text" id="inputGroup-sizing-default"
                  >Time Stamp</span
                >
                <input
                  type="text"
                  class="form-control"
                  aria-label="Sizing example input"
                  aria-describedby="inputGroup-sizing-default"
                  name="timestamp"
                  v-model="timestamp"
                />
              </div>
              <div
                v-if="
                  $store.getters.get_selected_tracker.tracker_type ==
                    'Multiple Choice' ||
                  $store.getters.get_selected_tracker.tracker_type == 'Boolean'
                "
              >
                <div class="input-group mb-3">
                  <span class="input-group-text" id="inputGroup-sizing-default"
                    >Value</span
                  >
                  <select
                    class="form-select form-control mb-3"
                    aria-label="Sizing example input"
                    name="value"
                    v-model="value"
                  >
                    <option
                      v-for="each in $store.getters.get_selected_tracker
                        .reqd_values_list"
                      :key="each.index"
                      :value="each"
                    >
                      {{ each }}
                    </option>
                  </select>
                </div>
              </div>

              <div v-else>
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
                <button
                  type="submit"
                  class="btn btn-primary"
                  @click="submitLogForm($event)"
                >
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
    <!-- Log a value Modal -->
  </div>
</template>

<script>
import getCurrentTimestamp from "../../utils/getCurrentTimeStamp";
import FetchFunction from "@/utils";
export default {
  name: "LogValueModal",
  mounted() {
    this.error = false;
    this.error_msg = "";
    this.value = "";
    this.note = "";
  },
  data() {
    return {
      error: false,
      reeor_msg: "",
      timestamp: "",
      value: "",
      note: "",
    };
  },
  methods: {
    async submitLogForm(e) {
      e.preventDefault();
      let data = {
        tracker_id: this.$store.getters.get_selected_tracker.id,
        time_stamp: this.timestamp,
        value: this.value,
        note: this.note,
      };
      let url = "http://localhost:5000/api/trackerLogs/post";
      let init_obj = {
        method: "POST",
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
          $("#logValueModal").modal("hide");
          await this.$store.dispatch("getTrackers");
          await this.$store.dispatch("getSelectedTrackerDetails");
          await this.$store.dispatch('getDataSummary');
        })
        .catch((e) => {
          this.error_msg = JSON.parse(e.message).error_message;
          this.error = true;
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
    generateTimestamp(e) {
      e.preventDefault();
      this.value = "";
      this.note = "";
      this.timestamp = getCurrentTimestamp();
    },
  },
};
</script>
