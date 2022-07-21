# calculate-taxi-fare
Problem statement:
The table below shows different charge rates for a trip, provided for different time
categories (all 24 hrs included). Create a Django application to take the distance
covered by the vehicle (in KM) and time (in hh: mm format) as input and
calculate the final trip fare.

Solution: 
A. For this problem I have used three models.
  1. Image
  2. Price 
  3. Fare

B. I have used one view:  FareCreate(TemplateView)
  view consists of two methods.
    1. Get method which is used to display form on template view.
    
    2. Post method which is used to calculate the fare.
      Fare is calulated as follows:-
            t1 = form.cleaned_data['time']
            distance = form.cleaned_data['distance']
            distance = int(distance)
            price = Price.objects.get(time__time=str(t1))
            surge = (int(price.surge_charge) / 100) + 1
            service = (int(price.service_charge) / 100) + 1
            result = int(price.initial_charge) + distance * int(price.km_rate) * surge * service
  
  C.Output
    ![image](https://user-images.githubusercontent.com/58128009/180229983-211ff0d8-141b-4274-be63-43f85df0bfc8.png)
