<template>
    <div class="information" v-if="cardItem!=null">
        <div class="information__head">
            <h4>{{ cardItem.name }}</h4>
            <span>{{ cardItem.objectType }}</span>
            <div class="menu">
                <span class="menu__button" :class="{active: this.menu.desc === true}" @click="setDesc()">Описание</span>
                <span class="menu__button" :class="{active: this.menu.graph === true}" @click="setGraph()">График</span>
                <span class="menu__button" :class="{active: this.menu.contact === true}" @click="setContact()">Контакты</span>
            </div>
        </div>
        <div class="information__text" v-if="this.menu.desc === true">
            <span class="desc">{{ cardItem.desc }}</span>
            <div class="information__text-block" v-if="cardItem.sportType != null">
                <div class="icon">
                    <base-svg name="volleyball"></base-svg>
                </div>
                <div class="info">
                    <span class="head-span">Виды спорта</span>
                    <span class="info-span">{{ cardItem.sportType }}</span>
                </div>
            </div>
            <div class="information__text-block" v-if="cardItem.address != null">
                <div class="icon">
                    <base-svg name="geo" class="geo-svg"></base-svg>
                </div>
                <div class="info">
                    <span class="head-span">Адресс</span>
                    <span class="info-span">{{ cardItem.address }}</span>
                </div>
            </div>
            <div class="information__text-block" v-if="cardItem.phone != null">
                <div class="icon">
                    <base-svg name="phone"></base-svg>
                </div>
                <div class="info">
                    <span class="head-span">Телефон</span>
                    <span class="info-span">{{ cardItem.phone }}</span>
                </div>
            </div>
            <div class="information__text-block" v-if="cardItem.workingTime != null">
                <div class="icon">
                    <base-svg name="timer"></base-svg>
                </div>
                <div class="info">
                    <span class="head-span">Рабочее время</span>
                    <span class="info-span">{{ cardItem.workingTime }}</span>
                </div>
            </div>
            <!-- <div class="information__text-block" v-if="cardItem.action != null">
                <div class="icon">
                    <base-svg name="hammer"></base-svg>
                </div>
                <div class="info">
                    <span class="head-span">Действие с объектом</span>
                    <span class="info-span">{{ cardItem.action }}</span>
                </div>
            </div> -->
            <!-- <span>Активный: {{ (cardItem.active === 'Y') ? 'Да' : 'Нет' }}</span> -->
        </div>
        <div class="information__text" v-if="this.menu.graph === true">  
            <div class="information__text-block graphic" v-if="showGraph">
                <div class="info">
                    <span class="head-span">График финансирования</span>
                </div>
                <blocks-pie-finance :idObject="cardItem.id" ref="graph"></blocks-pie-finance>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        cardItem: {
            type: Object,
            default: null,
        },
        showGraph: {
            type: Boolean,
            default: true,
        }
    },
    data: () => ({
        menu: {
            desc: true,
            graph: false,
            contact: false,
        }
    }),
    methods: {
        setDesc() {
            this.menu = {
                desc: true,
                graph: false,
                contact: false,
            }
        },
        setGraph() {
            this.menu = {
                desc: false,
                graph: true,
                contact: false,
            }
        },
        setContact() {
            this.menu = {
                desc: false,
                graph: false,
                contact: true,
            }
        }
    }
}
</script>

<style lang="scss" scoped>
.menu {
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    margin-bottom: 20px;

    &__button {
        padding: 10px 20px;
        border-bottom: 3px solid $color-7;
        transition: all 0.8s ease;
        border-radius: 10px 10px 0 0;
        font-weight: 500;
        color: $color-7;
        cursor: pointer;

        &:hover {
            background-color: $color-4;
            border-radius: 10px;
        }
    }

    .active {
        border-bottom: 3px solid $color-3;
        // color: $color-3;
    }
}
.desc {
    color: #212121;
    line-height: 20px;
}
.information {
    transition: all 5s ease;

    &__head {
        display: flex;
        flex-direction: column;
    }

    &__text {
        // padding-top: 10px;
        display: flex;
        flex-direction: column;

        &-block {
            display: flex;
            flex-direction: row;
            align-items: center;
            padding: 10px 0;
            border-bottom: 1px solid #f7f7f7;

            .icon {
                margin-right: 20px;

                .svg {
                    width: 32px;
                    height: auto;

                    :deep() svg {
                        max-width: 100%;
                        max-height: 100%;
                    }
                }

                .geo-svg {
                    width: 28px;
                }
            }

            .info {
                display: flex;
                flex-direction: column;

                .head-span {
                    font-weight: 600;
                    color: #212121;
                    font-size: 17px;
                    padding-bottom: 5px;
                }

                .info-span {
                    font-weight: 400;
                    color: #808080;
                    font-size: 17px;
                    padding-bottom: 0;
                }
            }
        }

        .graphic {
            flex-direction: column;
            
        }
    }

    h4 {
        font-size: 26px;
        padding-bottom: 5px;
        color: #212121;
    }
    span {
        font-size: 17px;
        color: #808080;
        padding-bottom: 10px;
    }
}
</style>