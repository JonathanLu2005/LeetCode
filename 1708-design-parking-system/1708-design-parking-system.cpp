class ParkingSystem {
    map<int, int> myMap;
public:
    ParkingSystem(int big, int medium, int small) {
        myMap = { {1, big}, {2, medium}, {3, small} };
    }
    
    bool addCar(int carType) {
        if (myMap[carType] == 0) {
            return false;
        }

        myMap[carType] -= 1;
        return true;
    }
};

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem* obj = new ParkingSystem(big, medium, small);
 * bool param_1 = obj->addCar(carType);
 */