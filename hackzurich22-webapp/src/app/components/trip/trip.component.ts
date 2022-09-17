import { Component, OnInit } from '@angular/core';
import { WsService } from 'src/app/services/ws.service';

type State =
  "enteredBuilding" |
  "walkingStairs" |
  "waitingForElevator" |
  "boardingElevator" |
  "raidingElevator" |
  "unBoardingElevator" |
  "onTargetFloor" |
  "arrivedAtDestination" |
  "leftBuilding";

@Component({
  selector: 'app-trip',
  templateUrl: './trip.component.html',
  styleUrls: ['./trip.component.scss']
})
export class TripComponent {

  customerState: State = "enteredBuilding";

  currentFloor = 0;

  travelDuration = '3 Minutes';

  customerName = "Jacqueline";

  identityCode = "AC15"

  targetFloor = "4th";

  elevatorId = "E";

  stopsToTarget = 0;

  roomToGo = '404';

  pacientName = 'Rosmarie Meier'

  showingLostPopUp = false;

  didUseElevator = false;

  onReturnWay = false;

  exitPoint = "Parking Level 2";

  constructor(private wsService: WsService) { }

  timeouts: any[] = [];

  orderElevator() {
    this.customerState = "waitingForElevator";
    this.didUseElevator = true;

    this.timeouts.push(setTimeout(() => {
      this.customerState = "boardingElevator";
      this.travelDuration = "2 min 30sec";
    }, 2000))
    this.timeouts.push(setTimeout(() => {
      this.customerState = "raidingElevator";
      this.travelDuration = "2 min";
    }, 5000))
    this.timeouts.push(setTimeout(() => this.customerState = "unBoardingElevator", 7000))
    this.timeouts.push(setTimeout(() => {
      this.customerState = "onTargetFloor"
      this.travelDuration = "30 sec";
    }, 9000))
  }

  goBack() {
    this.customerState = "enteredBuilding";
    this.onReturnWay = true;
  }

  missedElevator() {
    this.timeouts.forEach(timeout => clearTimeout(timeout));
    this.orderElevator();
  }

  didNotUnboard() {
    this.showingLostPopUp = true;
    this.timeouts.forEach(timeout => clearTimeout(timeout));
  }

  startOver(floorToStartFrom: number) {
    this.showingLostPopUp = false;

    this.customerState = "enteredBuilding";
  }

  gotLost() {
    this.showingLostPopUp = true;

  }

  startWalking() {
    this.didUseElevator = false;

    this.customerState = 'walkingStairs';
  }

  walkingCompleted() {
    this.customerState = 'onTargetFloor';
  }

  changeFromWalingToElevator() {
    this.showingLostPopUp = true;
  }

  arrived() {
    this.customerState = "arrivedAtDestination"
  }

  emergency() {
    alert('doctor is on the way')
  }
}
