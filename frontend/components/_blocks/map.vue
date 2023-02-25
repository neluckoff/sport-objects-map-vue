<template>
    <div class="container">
        <div class="row">
            <div class="col-xxl-12">
                <div class="map">
                    <client-only>
                        <l-map :zoom=13 :center="[61.374, 63.5594]">
                            <l-tile-layer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"></l-tile-layer>
                            <l-marker :lat-lng="[61.374, 63.5594]"></l-marker>
                            <!-- <template v-for="(item, i) in items">
                                <l-marker :lat-lng="[61.374, 63.5594]"></l-marker>
                            </template> -->
                            <!-- <l-marker :lat-lng="[61.374, 63.5594]">
                                <l-icon>
                                    <div class="marker">
                                        <div class="marker-icon">
                                            <base-svg name="location"></base-svg>
                                        </div>
                                    </div>
                                </l-icon> 
                            </l-marker> -->
                        </l-map>
                    </client-only>
                </div>
            </div>
        </div>
        <div class="row">
            <!-- <template v-for="(item, i) in items">
                <span>{{ item }}</span>
            </template> -->
            <span>{{ items }}</span>
        </div>
    </div>
</template>

<script>
export default {
    data: () => ({
		items: [{}],
    }),
    methods: {
		async fetch() {
			try {
				if (!this.add) {
					let response = await this.$axios.$get(
						`http://127.0.0.1:3000/api/v1/objects`,
						{}
						//this.config
					);
                    console.log(response)
					if (response) {
						this.items = response;
					}
				}
			} catch (err) {
				console.log(err);
			}
		},
	},
	mounted() {
		this.fetch()
	},
}
</script>

<style lang="scss" scoped>
.map {
    margin-top: 100px;
    width: 100%;
    height: 500px;

    :deep(.leaflet-container) {
		// background: #39494f;
		//background: #333;
		.leaflet-control-attribution {
			display: none !important;
		}
		.leaflet-control-zoom {
			display: none;
		}
	}

    .marker {
        padding-bottom: -28px;
    }
}
</style>
  