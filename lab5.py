> Łukaszynka:
class ImageAligning(BaseImage):
    """
    klasa odpowiadająca za wyrównywanie hostogramu
    """
    def init(self, path: str) -> None:
        super().init(path)

    def align_image(self, tail_elimination: bool = True) -> 'BaseImage':
        if(tail_elimination==False):
            if(self.data.ndim==2):
                min = self.data[0, 1]
                max = self.data[0, 1]
                for i in range(self.data.shape[0]):
                    for j in range(1, self.data.shape[1]):
                        pixel = (self.data[i, j])
                        if(pixel<min):
                            min = pixel
                        if(pixel>max):
                            max = pixel
            else:
                minr = self.data[0, 1, 0]
                maxr = self.data[0, 1, 0]
                ming = self.data[0, 1, 1]
                maxg = self.data[0, 1, 1]
                minb = self.data[0, 1, 2]
                maxb = self.data[0, 1, 2]
                for i in range(self.data.shape[0]):
                    for j in range(1, self.data.shape[1]):
                        pixel = (self.data[i, j])
                        if (pixel[0] < minr):
                            minr = pixel[0]
                        if (pixel[0] > maxr):
                            maxr = pixel[0]
                        if (pixel[1] < ming):
                            ming = pixel[1]
                        if (pixel[1] > maxg):
                            maxg = pixel[1]
                        if (pixel[2] < minb):
                            minr = pixel[2]
                        if (pixel[2] > maxb):
                            maxr = pixel[2]
        else:
            hist = Histogram(self.data).to_cumulated()
            if (self.data.ndim == 2):
                min = np.quantile(hist, 5)
                max = np.quantile(hist, 95)
            else:
                minr = np.quantile(hist[0], 5)
                maxr = np.quantile(hist[0], 95)
                ming = np.quantile(hist[1], 5)
                maxg = np.quantile(hist[1], 95)
                minb = np.quantile(hist[2], 5)
                maxb = np.quantile(hist[2], 95)


        if (self.data.ndim == 2):
            newPic = np.arange(self.data.shape[0] * self.data.shape[1]).reshape(self.data.shape[0], self.data.shape[1])
            for i in range(self.data.shape[0]):
                for j in range(1, self.data.shape[1]):
                    pixel = (self.data[i, j])
                    newPixel = (pixel - min) * (255 / (max - min))
                    newPic[i, j] = newPixel
            result = BaseImage("lena.jpg")
            result.data = newPic.astype(np.uint8)
            result.color_model = 1
            return result
        else:
            newPic = np.arange(self.data.shape[0] * self.data.shape[1] * 3).reshape(self.data.shape[0],
                                                                                    self.data.shape[1], 3)
            for i in range(self.data.shape[0]):
                for j in range(1, self.data.shape[1]):
                    pixel = (self.data[i, j])
                    newPixelRed = (pixel[0] - minr) * (255 / (maxr - minr))
                    newPixelGreen = (pixel[1] - ming) * (255 / (maxg - ming))
                    newPixelBlue = (pixel[2] - minb) * (255 / (maxb - minb))
                    newPic[i, j, 0] = newPixelRed
                    newPic[i, j, 1] = newPixelGreen
                    newPic[i, j, 2] = newPixelBlue
            result = BaseImage("lena.jpg")
            result.data = newPic.astype(np.uint8)
            result.color_model = 1
            return result

> Łukaszynka:
class Histogram:
    """
    klasa reprezentujaca histogram danego obrazu
    """
    values: np.ndarray  # atrybut przechowujacy wartosci histogramu danego obrazu
    histValuesArray: np.ndarray

    def init(self, values: np.ndarray) -> None:
        self.values = values
        self.histValuesArray = np.zeros(256)
        pass

    def histValues(self):
        if(self.values.ndim==2):
            tabOfGreys = np.zeros(256)
            for i in range(self.values.shape[0]):
                for j in range(self.values.shape[1]):
                    G = int(self.values[i, j])
                    tabOfGreys[G] += 1
            self.histValuesArray = tabOfGreys
        else:
            tabOfReds = np.zeros(256)
            tabOfGreens = np.zeros(256)
            tabOfBlues = np.zeros(256)
            for i in range(self.values.shape[0]):
                for j in range(self.values.shape[1]):
                    R = int(self.values[i, j, 0])
                    G = int(self.values[i, j, 1])
                    B = int(self.values[i, j, 2])
                    tabOfReds[R] += 1
                    tabOfGreens[G] += 1
                    tabOfBlues[B] += 1
            self.histValuesArray = np.array([tabOfReds, tabOfGreens, tabOfBlues])

    def plot(self) -> None:
        if (self.values.ndim == 2):
            plt.plot(self.histValuesArray, 'grey')
            plt.show()
        else:
            plt.subplots_adjust(wspace=0.5)
            plt.subplot(1, 3, 1)
            plt.plot(self.histValuesArray[0], 'red')
            plt.subplot(1, 3, 2)
            plt.plot(self.histValuesArray[1], 'green')
            plt.subplot(1, 3, 3)
            plt.plot(self.histValuesArray[2], 'blue')
            plt.show()

        pass

    def to_cumulated(self) -> 'Histogram':
        if(self.histValuesArray.ndim==1):
            hist = np.zeros(256)
            sum=0
            for i in range(255):
                sum=sum+self.histValuesArray[i]
                hist[i]=sum
            result = Histogram(self.values)
            result.histValuesArray = hist
            return result
        else:
            histR = np.zeros(256)
            histG = np.zeros(256)
            histB = np.zeros(256)
            sumR = 0
            sumG = 0
            sumB = 0
            for i in range(255):
                sumR = sumR + self.histValuesArray[0][i]
                sumG = sumG + self.histValuesArray[1][i]
                sumB = sumB + self.histValuesArray[2][i]
                histR[i] = sumR
                histG[i] = sumG
                histB[i] = sumB
            histOfColors: np.ndarray
            result = Histogram(self.values)
            result.histValuesArray = np.array([histR, histG, histB])
            return result
        pass
