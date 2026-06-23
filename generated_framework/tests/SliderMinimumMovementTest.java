package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.HorizontalSliderPage;

public class SliderMinimumMovementTest extends BaseTest {

    @Test
    public void sliderMinimumMovement() {

        HorizontalSliderPage page = new HorizontalSliderPage(driver);

        wait.until(ExpectedConditions.visibilityOf(page.get_input_0()));
        page.get_input_0().sendKeys("TEST_DATA");

        wait.until(ExpectedConditions.visibilityOf(page.get_input_0()));
        Assert.assertTrue(driver.getCurrentUrl().contains("dashboard"));

    }

}