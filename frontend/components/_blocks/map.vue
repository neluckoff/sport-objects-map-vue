<template>
    <section>
        <transition name="fadeWidth">
            <div class="object" v-if="cardItem!=null">
                <cards-object :cardItem="cardItem" :showGraph="showGraph" @toggle-button="closeDesc()"></cards-object>
            </div>
        </transition>
        <div class="map">
            <client-only>
                <div class="header">
                    <div class="header__left">
                        <div class="header__image">
                            <base-svg name="map"></base-svg>
                        </div>
                        <div class="header__text">
                            <span class="header__text-basic">
                                <span class="header__text-red">Карта</span> 
                                Спорта
                            </span>
                        </div>
                    </div>
                    <div class="header__settings">
                        <input class="input" type="text" placeholder="Поиск" v-model="searchText" v-on:keyup.enter="search"/>
                        <button type="button" class="search-btn" @click="search">
                            <base-svg name="search" class="icon"></base-svg>
                        </button>
                    </div>
                </div>
                <div class="settings">
                    <div class="settings__logo" @click="settings">
                        <base-svg name="gear"></base-svg>
                    </div>
                    <transition name="fade-height">
                        <div class="settings__params" v-if="showSettings == true">
                            <div class="settings__span">
                                <span>Настройки карты</span>
                            </div>
                            <div class="settings__params-map select-wrapper">
                                <select v-model="mapSelected" class="select">
                                    <option>Спутниковая</option>
                                    <option>Географическая</option>
                                    <option>Гибридная</option>
                                    <option>Рельефная</option>
                                </select>
                            </div>
                            <div class="settings__params-checkboxes">
                                <base-checkbox v-model="pointGroup" class="checkbox">
                                    <p>Группировка объектов</p>
                                </base-checkbox>
                            </div>
                            <div class="settings__params-radio radio-group">
                                <label>
                                    <input type="radio" name="radio" v-model="radioGroup" value="open" checked/>
                                    <span>Только активные</span>
                                </label>
                                <label>
                                    <input type="radio" name="radio" v-model="radioGroup" value="closed"/>
                                    <span>Только неактивные</span>
                                </label>
                            </div>
                        </div>
                    </transition>
                </div>
                <transition name="fade-height">
                    <div class="close-info" @click="closeDesc()" v-if="cardItem != null">
                        <base-svg name="chevron-left"></base-svg>
                    </div>
                </transition>
                <div class="num-objects">
                    <base-svg name="geo"></base-svg>
                    <span>{{ items.length }}</span>
                </div>
                <v-map :zoom=" options.minZoom" :center="center" :maxBounds="bounds" :maxBoundsViscosity="0.5" ref="map" @update:zoom="zoomUpdate">
                    <v-icondefault></v-icondefault>
                    <l-tile-layer :url="map" :options="options"></l-tile-layer>
                    <v-marker-cluster v-if="pointGroup">
                        <template v-for="(item, i) in items">
                            <v-marker @click="openDesc(item)" :lat-lng="[item.coordinates.lat, item.coordinates.lng]" :key="i">
                                <l-icon>
                                    <div class="marker">
                                        <div class="marker-icon">
                                            <base-marker name="dumbbell"></base-marker>
                                        </div>
                                    </div>
                                </l-icon>
                            </v-marker>
                        </template>
                    </v-marker-cluster>
                    <template v-for="(item, i) in items" v-else>
                        <v-marker @click="openDesc(item)" :lat-lng="[item.coordinates.lat, item.coordinates.lng]" :key="i">
                            <l-icon>
                                <div class="marker">
                                    <div class="marker-icon">
                                        <base-marker name="dumbbell"></base-marker>
                                    </div>
                                </div>
                            </l-icon>
                        </v-marker>
                    </template>
                </v-map>
            </client-only>
        </div>
    </section>
</template>

<script>
export default {
    
    data: () => ({
		items: [],
        bounds: [[-89.98155760646617, -180], [89.99346179538875, 180]],
        options: {
            minZoom: 3,
            maxZoom: 18,
            subdomains:['mt0','mt1','mt2','mt3'],
            noWrap: false,
        },
        center: [60, 0],
        map: 'http://{s}.google.com/vt/lyrs=s,h&x={x}&y={y}&z={z}', //http://{s}.google.com/vt/lyrs=s,h&x={x}&y={y}&z={z}
        mapSelected: "Гибридная",
        pointGroup: true,
        cardItem: null,
        showGraph: true,
        showSettings: false,
        currentZoom: null,
        searchText: "",
        radioGroup: "open",
	}),
	methods: {
		async fetch() {
			try {
				if (!this.add) {
					let response = await this.$axios.$get(
						`/api/v1/objects/?active=True`,
						{}
					);
					if (response) {
						this.items = response;
					}
				}
			} catch (err) {
				console.log(err);
			}
		},
        async fetchClosed() {
			try {
				if (!this.add) {
					let response = await this.$axios.$get(
						`/api/v1/objects/?active=false`,
						{}
					);
					if (response) {
						this.items = response;
					}
				}
			} catch (err) {
				console.log(err);
			}
		},
        async search() {
            console.log(this.searchText.length)
            if (this.searchText.length != 0) {
                try {
                    if (!this.add) {
                        let response = await this.$axios.$get(
                            `/api/v1/objects/?search=${this.searchText}`,
                            {}
                        );
                        if (response) {
                            this.items = response;
                        }
                    }
                } catch (err) {
                    console.log(err);
                }
            } else {
                this.fetch()
            }
		},
        async openDesc(item) {
            if (this.cardItem == null) {
                this.cardItem = item;
                setTimeout(() => {
                    this.reloadMap();
                }, 1000);
            } else {
                this.cardItem = item;
                this.reloadMap();
            }
            this.reloadManual()
            document.title = `${this.cardItem.name} - Карта Спорта`
        },
        async reloadManual() {
            this.showGraph = false;
            this.$nextTick(() => {
                this.showGraph = true;
            });
        },
        async closeDesc() {
            this.cardItem = null;
            setTimeout(() => {
                this.$refs.map.mapObject.invalidateSize(true);
            }, 680)
            this.$nuxt.refresh();
            document.title = `Карта Спорта`
        },
        async reloadMap() {
            this.$refs.map.mapObject.invalidateSize(true);
            this.$refs.map.mapObject.setView([this.cardItem.coordinates.lat, this.cardItem.coordinates.lng], this.currentZoom, {
                animate: true,
                duration: 1.0,
                
            });
        },
        async zoomUpdate(zoom) {
            this.currentZoom = zoom;
        },
        async settings() {
            if (this.showSettings == false) {
                this.showSettings = true;
            } else {
                this.showSettings = false;
            }
        }
	},
    watch: {
        mapSelected(newValue, oldValue) {
            if (newValue === "Спутниковая") {
                this.map = "http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}"
            } else if (newValue === "Географическая") {
                this.map = "http://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}"
            } else if (newValue === "Гибридная") {
                this.map = "http://{s}.google.com/vt/lyrs=s,h&x={x}&y={y}&z={z}"
            } else if (newValue === "Рельефная") {
                this.map = "http://{s}.google.com/vt/lyrs=p&x={x}&y={y}&z={z}"
            }
        },
        radioGroup(newValue, oldValue) {
            if (newValue === "open") {
                this.fetch()
            } else {
                this.fetchClosed()
            }
        },
    },
	mounted() {
		this.fetch()
	}
}
</script>

<style lang="scss" scoped>
section {
    display: flex;
    flex-direction: row;
}

.num-objects {
    display: flex;
    position: absolute;
    flex-direction: row;
    z-index: 999;
    bottom: 20px;
    right: 30px;
    // background-color: rgba(209, 209, 209, 0.5);
    backdrop-filter: blur(8px);
    background-color: rgba(30,30,30,0.5);
    padding: 10px 15px;
    border-radius: 10px;
    align-items: center;

    span {
        padding-left: 10px;
        color: $color-1;
        font-size: 18px;
        font-weight: 500;
    }

    .svg {
        width: 20px;
        height: auto;
        
        :deep() svg {
            fill: $color-3;
        }
    }
}

// ---------------------- //
.fadeWidth-enter-active, .fadeWidth-leave-active {
  transition: all 1s;
  max-width: 30%;
//   padding: 50px;
}
.fadeWidth-enter, .fadeWidth-leave-to {
  opacity: 0;
  max-width: 0px;
//   padding: 0;
}

.fade-height-enter-active, .fade-height-leave-active {
  transition: all 0.8s;
  max-height: 30%;
}
.fade-height-enter, .fade-height-leave-to {
  opacity: 0;
  max-height: 0px;
}

.close-info {
    position: absolute;
    z-index: 999;
    margin: auto;
    position: absolute;
    top: calc(50% - 40px);
    left: 0;
    height: 80px;
    width: 26px;
    backdrop-filter: blur(8px);
    background-color: rgba(30,30,30,0.5);
    cursor: pointer;
    border-radius: 0 10px 10px 0;
    transition: all .2s ease-out;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.6s;
    

    .svg {
        width: 10px;
        height: auto;
        
        :deep() svg {
            fill: $color-7;
            transition: all 0.6s;
        }
    }

    &:hover {
        width: 30px;
        .svg {
            :deep() svg {
                fill: $color-1; 
            }
        }
    }
}

.object {
    overflow-y: auto;
    overflow-x: hidden;;
    box-shadow: 0px 0px 40px rgba(0, 0, 0, 0.13);
    right: 0;
    height: 100vh;
    width: 30%;
    background-color: $color-1;
    // padding: 0;
}

.settings {
    z-index: 999;
    position: absolute;
    right: 30px;
    top: 20px;
    transition: all 0.3s ease-out;
    display: flex;
    flex-direction: column;
    align-items: flex-end;

    &__span {
        padding-bottom: 5px;

        span { 
            color: $color-1;
            font-weight: 500;
        }
    }

    &__params {
        margin-top: 10px;
        padding: 20px;
        backdrop-filter: blur(8px);
        background-color: rgba(30,30,30,0.5);
        border-radius: 10px;
        box-shadow: 0px 0px 40px rgba(0, 0, 0, 0.13);

        &-map {
            margin-bottom: 7px;;
        }

        &-checkboxes {
            border-top: 1px solid $color-7;
            border-bottom: 1px solid $color-7;
            padding: 10px 0;
        }

        &-radio {
            padding-top: 10px;
        }
    }

    &__logo {
        box-shadow: 0px 0px 40px rgba(0, 0, 0, 0.13);
        padding: 10px;
        backdrop-filter: blur(8px);
        background-color: rgba(30,30,30,0.5);
        border-radius: 10px;
        cursor: pointer;

        &:hover {
            opacity: 0.8;
        }
        .svg {
            width: 100%;
            height: 100%;
            justify-content: center;
            align-items: center;
            
            :deep() svg {
                fill: $color-3;
                width: 28px;
                height: auto;
            }
        }
    }
}

.header {
    top: 20px;
    left: 30px;
    z-index: 999;
    position: absolute;
    display: flex;
    flex-direction: row;
    align-items: center;

    &__settings {
        box-shadow: 0px 0px 40px rgba(0, 0, 0, 0.13);
        backdrop-filter: blur(8px);
        background-color: rgba(30,30,30,0.5);
        height: 48px;
        border-radius: 10px;
        margin-left: 10px;
        cursor: pointer;
        transition: all .2s ease-out;

        .svg {
            width: 28px;
            height: auto;
            
            :deep() svg {
                fill: $color-3;
            }
        }

        width: auto;
		position: relative;
		display: inline-flex;
		flex-direction: row;
		justify-content: space-between;
		align-items: center;

		.search-btn {
			background-color: transparent;
			position: absolute;
			right: 12px;
			width: 40px;
			cursor: pointer;
			.icon {
				:deep() svg {
					width: 100%;
					height: auto;
					max-width: 24px;
					max-height: 24px;
				}
			}
		}
		.input {
			display: flex;
			border: none;
			padding: 12px 60px 12px 18px;
			border-radius: 10px;
			background-color: transparent;
			width: 100%;
			max-width: 200px;
			height: 100%;
			color: $color-1;
			font-size: 18px;
			font-weight: 500;
			border: 2px solid transparent;
			transition: 0.1s ease-in-out;
			&:focus {
				outline: none;
				// border: 2px solid $color-3;
				color: $color-1;
				max-width: 350px;
			}
            &::placeholder {
                color: $color-7;
            }
		}
    }

    &__left {
        box-shadow: 0px 0px 40px rgba(0, 0, 0, 0.13);
        padding: 0 20px;
        height: 48px;
        backdrop-filter: blur(8px);
        background-color: rgba(30,30,30,0.5);
        border-radius: 10px;
        // width: 100%;
        display: inline-flex;
        flex-direction: row;
        align-items: center;
    }

    &__image {
        margin-right: 20px;

        .svg {
            width: 30px;
            height: auto;
            
            :deep() svg {
                fill: $color-3;
            }
        }
    }

    &__text {
        &-basic {
            color: $color-1;
            font-size: 20px;
            font-weight: 600;
        }

        &-red {
            font-size: 20px;
            color: $color-3;
        }
    }
}
.map {
    overflow: hidden;
    z-index: 1;
    width: 100%;
    height: 100vh;
    display: flex;
    flex-direction: row;
    position: relative;

    :deep(.leaflet-container) {
        .leaflet-control-attribution {
            display: none !important;
        }
        .leaflet-control-zoom {
            display: none;
        }
    }
    .marker {
        .svg {
            box-shadow: 0px 0px 40px rgba(0, 0, 0, 0.13);
            background-color: $color-3;
            padding: 5px;
            border-radius: 50%;
            border: 2px solid rgba(33, 33, 33, 0.5);

            width: 26px;
            height: 26px;

            :deep() svg {
                max-width: 100%;
                max-height: 100%;
            }

            &:hover {
                opacity: 0.8;
            }
        }
    }
}

@media screen and (max-width: $screen-md) {
	.header {
        left: 0;

        &__left {
            display: none;
        }
    }

    .settings {
        right: 10px;
    }

    .num-objects {
        right: 10px;
    }

    .object {
        position: absolute;
        z-index: 9999;
        width: 100%;
    }

    .fadeWidth-enter-active, .fadeWidth-leave-active {
        transition: all 1s;
        max-width: 100%;
    }
    .fadeWidth-enter, .fadeWidth-leave-to {
        opacity: 0;
        max-width: 0;
    }

    .close-info {
        display: none;
    }
}
</style>