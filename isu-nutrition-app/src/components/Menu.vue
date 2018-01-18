<template>
    <div>
        <br>
        <h3> {{diningCenterName}} </h3>
        <h5> 
             <span @click="decrementDate()" class="date-arrow"> <a> <<<< </a> </span> 
            {{dateString}} 
           <a> <span @click="incrementDate()" class="date-arrow"> >>>> </span> </a>
        </h5>

        <select v-model="selectedMeal" class="form-control">
            <option value="all">All </option>
            <option  v-for="(mealData,mealName) in menu" :value="mealName">{{mealName}}</option> 
        </select>
        <br>
        
        <div  v-for="(stationData, stationName) in menu[selectedMeal]">
            <h5> {{ stationName }} </h5>
            <table class="table">
                <tbody>
                    <tr  v-for="food in stationData">
                        <td> <b> {{food.name}} </b> <br> ({{food.servingSize}})</td>
                        <td class='macros'>
                        <span> <b> {{food.calories}} </b> </span>
                            | <span style="color:red">{{formatMacros(food['fat'])}} </span>
                            | <span style="color:green">{{formatMacros(food['carbs'])}} </span>
                            | <span style="color:blue">{{formatMacros(food['protein'])}} </span>
                        </td>
                    </tr>
                </tbody>
            </table> 
        </div> 
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        data(){
            return{
               diningCenterName:'',
               menu: {},
               selectedMeal:'',
               date: new Date(),
               dateString: ''
            }
        },
        computed: {
           
        },
        methods: {
            formatMacros:function(str){
                return isNaN(parseInt(str)) ? "<1":parseInt(str);
            },
            incrementDate(){
                this.date.setDate(this.date.getDate() + 1)
                this.update()
            },
            decrementDate() {
                this.date.setDate(this.date.getDate() - 1)
                this.update()
            },

            update() {
                this.menu = {}
                this.diningCenterName = this.$route.params.diningCenterName
                
                let monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
                let dateURL = monthNames[this.date.getMonth()] + '_' + this.date.getDate() + '_' + this.date.getFullYear()
                this.dateString =  monthNames[this.date.getMonth()] + ' ' + this.date.getDate() + ' ' + this.date.getFullYear()

                let url = 'https://sethpipho.github.io/isu-nutrition/isu-nutrition-data/data/' + this.diningCenterName.split(' ').join('_') + '/' + dateURL+ '.json' 

                axios.get(url)
                    .then(respone => {
                        this.menu = respone.data
                        this.selectedMeal = Object.keys(this.menu)[0]
                    })
                
            }
        },
         watch: {
            '$route' (to, from) {
                this.update()  
            }
        },
        mounted(){
            this.update()
        }
          
    }
</script>
<style>
    .food-row {
        border-bottom: 1px solid black;
    }
    .macros {
        text-align:right;
        min-width:10em;
    }
    .date-arrow{
        color:#9b4dca;
    }
</style>