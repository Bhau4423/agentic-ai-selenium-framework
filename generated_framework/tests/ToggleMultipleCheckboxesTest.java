package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.CheckboxesPage;

public class ToggleMultipleCheckboxesTest extends BaseTest {

    @Test
    public void toggleMultipleCheckboxes() {

        CheckboxesPage page = new CheckboxesPage(driver);



        Assert.assertTrue(driver.getCurrentUrl().contains("dashboard"));

    }

}