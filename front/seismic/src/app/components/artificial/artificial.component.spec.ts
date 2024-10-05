import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ArtificialComponent } from './artificial.component';

describe('ArtificialComponent', () => {
  let component: ArtificialComponent;
  let fixture: ComponentFixture<ArtificialComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ArtificialComponent]
    });
    fixture = TestBed.createComponent(ArtificialComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
