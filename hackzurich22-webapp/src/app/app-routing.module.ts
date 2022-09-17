import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DestinationPickerComponent } from './components/destination-picker/destination-picker.component';
import { TripComponent } from './components/trip/trip.component';

const routes: Routes = [
  {path: 'trip', component: TripComponent},
  {path: 'start', component: DestinationPickerComponent},
  {path: '', pathMatch: 'full', redirectTo: 'start'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
