import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { InsideScreenComponent } from './components/inside-screen/inside-screen.component';
import { OutsideScreenComponent } from './components/outside-screen/outside-screen.component';

const routes: Routes = [
  {path: 'inside', component: InsideScreenComponent},
  {path: 'outside', component: OutsideScreenComponent},
  {path: '', pathMatch: 'full', redirectTo: 'inside'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
