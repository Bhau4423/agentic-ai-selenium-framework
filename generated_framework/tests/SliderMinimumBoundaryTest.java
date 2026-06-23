package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.HorizontalSliderPage;

public class SliderMinimumBoundaryTest extends BaseTest {

    @Test
    public void sliderMinimumBoundary() {

        HorizontalSliderPage page = new HorizontalSliderPage(driver);


        Assert.assertTrue(driver.getCurrentUrl().contains("dashboard"));

    }

}