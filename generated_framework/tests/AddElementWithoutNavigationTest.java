package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.AddRemoveElementsPage;

public class AddElementWithoutNavigationTest extends BaseTest {

    @Test
    public void addElementWithoutNavigation() {

        AddRemoveElementsPage page = new AddRemoveElementsPage(driver);


        Assert.assertFalse(driver.getCurrentUrl().contains("dashboard"));

    }

}