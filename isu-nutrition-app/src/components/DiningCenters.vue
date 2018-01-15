<template>
    <div>
        <br>
       <h3> Dining Centers </h3>
       <hr>
       <div v-for="diningCenter in diningCenters">
            <router-link :to="diningCenter" > <h5> {{diningCenter}} </h5> </router-link>
            <hr>
        </div> 
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        data(){
            return{
                diningCenters: [],
            }
        },
     
        methods:{
          
        },
        mounted(){
           axios.get('https://sethpipho.github.io/isu-nutrition/isu-nutrition-data/data/dining-centers.json')
           .then(reponse => {
               this.diningCenters = reponse.data
           })
        }
    }
</script>
<style>

</style>